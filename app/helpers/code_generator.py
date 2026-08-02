import re

from app.database.connection import Database


class CodeGenerator:
    """
    Generates the next sequential code for a database table.

    Example:
        AST-000001
        SUP-000001
        PRT-000001
    """

    @staticmethod
    def next_code(
        table_name,
        field_name,
        prefix,
        digits=6
    ):
        CodeGenerator._validate_identifier(table_name)
        CodeGenerator._validate_identifier(field_name)

        conn = Database.connect()
        cursor = conn.cursor()

        try:
            cursor.execute(
                f"""
                SELECT {field_name}
                FROM {table_name}
                WHERE {field_name} LIKE ?
                ORDER BY id DESC
                LIMIT 1
                """,
                (f"{prefix}-%",)
            )

            row = cursor.fetchone()

        finally:
            conn.close()

        if row is None or not row[field_name]:
            return f"{prefix}-{1:0{digits}d}"

        current_code = str(row[field_name]).strip()

        match = re.fullmatch(
            rf"{re.escape(prefix)}-(\d+)",
            current_code
        )

        if match is None:
            raise ValueError(
                f"Invalid code format found in "
                f"{table_name}.{field_name}: {current_code}"
            )

        next_number = int(match.group(1)) + 1

        return f"{prefix}-{next_number:0{digits}d}"

    @staticmethod
    def _validate_identifier(identifier):
        """
        Prevent unsafe SQL table or column names.

        SQL parameters cannot be used for table and column names,
        so identifiers must be validated before being inserted
        into the SQL statement.
        """

        if not re.fullmatch(
            r"[A-Za-z_][A-Za-z0-9_]*",
            identifier
        ):
            raise ValueError(
                f"Invalid database identifier: {identifier}"
            )