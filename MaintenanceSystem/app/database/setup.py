from app.database.connection import Database
from app.database.schema import create_tables
from app.database.seed import (
    seed_default_admin,
    seed_app_settings,
    seed_lookup_tables,
    seed_preventive_maintenance
)
from app.database.migrations import MigrationManager


def setup_database():
    """Initialize the application database."""
    
    Database.initialize()
    
    create_tables()
    
    seed_default_admin()
    seed_app_settings()
    seed_lookup_tables()
    seed_preventive_maintenance()
    
    MigrationManager.run()