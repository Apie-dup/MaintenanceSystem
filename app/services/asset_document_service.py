
import os
import shutil
import uuid
from pathlib import Path

from app.database.connection import Database
from app.models.asset_document_model import AssetDocumentModel
from app.services.asset_service import AssetService
from app.core.auth_session import AuthSession


class AssetDocumentService:

    # ---------------------------------------------------------
    # Document authorization
    # ---------------------------------------------------------

    @staticmethod
    def require_permission(user, permission):
        """
        Authorize document operations using the
        current authenticated session.

        The user argument is retained temporarily
        for compatibility with existing dialogs.
        """

        AuthSession.require_permission(permission)

    # ---------------------------------------------------------
    # Managed document storage
    # ---------------------------------------------------------

    @staticmethod
    def storage_directory():
        database_path = Path(Database.database_path())

        return (
            database_path.parent.parent
            / "data"
            / "asset_documents"
        )

    # ---------------------------------------------------------
    # Read document information
    # ---------------------------------------------------------

    @staticmethod
    def get_by_asset(asset_id, *, user=None):

        AssetDocumentService.require_permission(
            user,
            "asset_documents"
        )

        return AssetDocumentModel.get_by_asset(
            asset_id
        )

    @staticmethod
    def get_by_id(
        document_id,
        *,
        asset_id,
        user=None,
    ):

        AssetDocumentService.require_permission(
            user,
            "asset_documents"
        )

        document = AssetDocumentModel.get_by_id(
            document_id
        )

        if document is None:
            return None

        if document["asset_id"] != asset_id:
            raise ValueError(
                "Document does not belong to this asset."
            )

        return document

    @staticmethod
    def search(
        asset_id,
        search_text,
        *,
        user=None,
    ):

        AssetDocumentService.require_permission(
            user,
            "asset_documents"
        )

        return AssetDocumentModel.search(
            asset_id,
            search_text
        )

    # ---------------------------------------------------------
    # Validate metadata
    # ---------------------------------------------------------

    @staticmethod
    def validate_metadata(data):
        if not str(data.get("document_name") or "").strip():
            raise ValueError(
                "Document name is required."
            )

        if not str(data.get("document_type") or "").strip():
            raise ValueError(
                "Document type is required."
            )

    # ---------------------------------------------------------
    # Add document
    # ---------------------------------------------------------

    @staticmethod
    def add_document(asset_id, source_file, data, *, user=None):

        AssetDocumentService.require_permission(
            user,
            "asset_documents.create"
        )

        AssetDocumentService.validate_metadata(data)

        if not AssetService.get_by_id(asset_id):
            raise ValueError("Asset does not exist.")

        source = Path(source_file).resolve(strict=True)

        if not source.is_file():
            raise ValueError(
                "The selected path is not a file."
            )

        storage = (
            AssetDocumentService.storage_directory()
            .resolve()
        )
        storage.mkdir(parents=True, exist_ok=True)

        stored_name = f"{uuid.uuid4().hex}{source.suffix.lower()}"
        destination = storage / stored_name

        try:
            shutil.copy2(source, destination)

            document_data = {
                "asset_id": asset_id,
                "document_name": data["document_name"].strip(),
                "document_type": data["document_type"].strip(),
                "description": data.get("description"),
                "file_name": source.name,
                "file_path": stored_name,
                "file_size": destination.stat().st_size,
                "expiry_date": data.get("expiry_date"),
                "uploaded_by": data.get("uploaded_by"),
            }

            return AssetDocumentModel.insert(document_data)

        except Exception:
            destination.unlink(missing_ok=True)
            raise

    # ---------------------------------------------------------
    # Resolve a managed document path
    # ---------------------------------------------------------

    @staticmethod
    def document_path(document):
        stored_name = document["file_path"]

        if (
            not stored_name
            or Path(stored_name).name != stored_name
            or stored_name in (".", "..")
            or "\\" in stored_name
        ):
            raise ValueError(
                "Invalid stored document path."
            )

        storage = (
            AssetDocumentService.storage_directory()
            .resolve()
        )

        return storage / stored_name

    # ---------------------------------------------------------
    # Open document
    # ---------------------------------------------------------

    @staticmethod
    def open_document(
        document_id,
        *,
        asset_id,
        user=None,
    ):

        AssetDocumentService.require_permission(
            user,
            "asset_documents"
        )

        document = AssetDocumentModel.get_by_id(
            document_id
        )

        if document is None:
            raise ValueError("Document not found.")

        if document["asset_id"] != asset_id:
            raise ValueError(
                "Document does not belong to this asset."
            )

        file_path = AssetDocumentService.document_path(
            document
        )

        if not file_path.is_file():
            raise FileNotFoundError(
                "The document file could not be found."
            )

        os.startfile(str(file_path))

    # ---------------------------------------------------------
    # Update document information
    # ---------------------------------------------------------

    @staticmethod
    def update_document(
        document_id,
        data,
        *,
        asset_id,
        user=None,
    ):

        AssetDocumentService.require_permission(
            user,
            "asset_documents.edit"
        )

        document = AssetDocumentModel.get_by_id(
            document_id
        )

        if document is None:
            raise ValueError(
                "Document not found."
            )

        if document["asset_id"] != asset_id:
            raise ValueError(
                "Document does not belong to this asset."
            )

        AssetDocumentService.validate_metadata(data)

        return AssetDocumentModel.update(
            document_id,
            {
                "document_name": data["document_name"].strip(),
                "document_type": data["document_type"].strip(),
                "description": data.get("description"),
                "expiry_date": data.get("expiry_date"),
            }
        )

    # ---------------------------------------------------------
    # Delete document
    # ---------------------------------------------------------

    @staticmethod
    def delete_document(
        document_id,
        *,
        asset_id,
        user=None,
    ):

        AssetDocumentService.require_permission(
            user,
            "asset_documents.delete"
        )

        document = AssetDocumentModel.get_by_id(document_id)

        if document is None:
            raise ValueError("Document not found.")

        if document["asset_id"] != asset_id:
            raise ValueError(
                "Document does not belong to this asset."
            )

        file_path = AssetDocumentService.document_path(document)

        # Move the file aside before deleting its database row.
        # This allows restoration if the database operation fails.
        temporary_path = None

        if file_path.exists():
            temporary_path = file_path.with_name(
                f"{file_path.name}.{uuid.uuid4().hex}.pending_delete"
            )
            file_path.rename(temporary_path)

        try:
            deleted = AssetDocumentModel.delete(document_id)

            if not deleted:
                raise RuntimeError(
                    "The document record could not be deleted."
                )

        except Exception:
            if temporary_path and temporary_path.exists():
                temporary_path.rename(file_path)
            raise

        if temporary_path:
            temporary_path.unlink()
