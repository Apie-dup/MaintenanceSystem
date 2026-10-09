
from app.database.connection import Database


class AssetDocumentModel:

    COLUMNS = """
        id,
        asset_id,
        document_name,
        document_type,
        description,
        file_name,
        file_path,
        file_size,
        upload_date,
        expiry_date,
        uploaded_by
    """

    # ---------------------------------------------------------
    # Get documents belonging to an asset
    # ---------------------------------------------------------

    @staticmethod
    def get_by_asset(asset_id):
        conn = Database.connect()

        try:
            return conn.execute(
                f"""
                SELECT {AssetDocumentModel.COLUMNS}
                FROM asset_documents
                WHERE asset_id = ?
                ORDER BY upload_date DESC, id DESC
                """,
                (asset_id,)
            ).fetchall()
        finally:
            conn.close()

    # ---------------------------------------------------------
    # Get document by ID
    # ---------------------------------------------------------

    @staticmethod
    def get_by_id(document_id):
        conn = Database.connect()

        try:
            return conn.execute(
                f"""
                SELECT {AssetDocumentModel.COLUMNS}
                FROM asset_documents
                WHERE id = ?
                """,
                (document_id,)
            ).fetchone()
        finally:
            conn.close()

    # ---------------------------------------------------------
    # Search documents for a specific asset
    # ---------------------------------------------------------

    @staticmethod
    def search(asset_id, search_text):
        conn = Database.connect()

        try:
            search = f"%{search_text}%"

            return conn.execute(
                f"""
                SELECT {AssetDocumentModel.COLUMNS}
                FROM asset_documents
                WHERE asset_id = ?
                  AND (
                      document_name LIKE ?
                      OR document_type LIKE ?
                      OR description LIKE ?
                      OR file_name LIKE ?
                  )
                ORDER BY upload_date DESC, id DESC
                """,
                (asset_id, search, search, search, search)
            ).fetchall()
        finally:
            conn.close()

    # ---------------------------------------------------------
    # Insert document metadata
    # ---------------------------------------------------------

    @staticmethod
    def insert(data):
        conn = Database.connect()

        try:
            cursor = conn.execute(
                """
                INSERT INTO asset_documents (
                    asset_id,
                    document_name,
                    document_type,
                    description,
                    file_name,
                    file_path,
                    file_size,
                    expiry_date,
                    uploaded_by
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    data["asset_id"],
                    data["document_name"],
                    data["document_type"],
                    data.get("description"),
                    data["file_name"],
                    data["file_path"],
                    data["file_size"],
                    data.get("expiry_date"),
                    data.get("uploaded_by"),
                )
            )

            conn.commit()
            return cursor.lastrowid

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    # ---------------------------------------------------------
    # Update document metadata
    # ---------------------------------------------------------

    @staticmethod
    def update(document_id, data):
        conn = Database.connect()

        try:
            cursor = conn.execute(
                """
                UPDATE asset_documents
                SET
                    document_name = ?,
                    document_type = ?,
                    description = ?,
                    expiry_date = ?
                WHERE id = ?
                """,
                (
                    data["document_name"],
                    data["document_type"],
                    data.get("description"),
                    data.get("expiry_date"),
                    document_id,
                )
            )

            conn.commit()
            return cursor.rowcount > 0

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    # ---------------------------------------------------------
    # Delete document metadata
    # ---------------------------------------------------------

    @staticmethod
    def delete(document_id):
        conn = Database.connect()

        try:
            cursor = conn.execute(
                """
                DELETE FROM asset_documents
                WHERE id = ?
                """,
                (document_id,)
            )

            conn.commit()
            return cursor.rowcount > 0

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()
