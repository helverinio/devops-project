#!/usr/bin/env python3
"""
Database initialization script for the blacklist microservice
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models.blacklist import BlacklistEntry

def init_database():
    """Initialize the database with tables"""
    app = create_app()
    
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("Database tables created successfully!")
        
        # Verify tables exist
        inspector = db.inspect(db.engine)
        tables = inspector.get_table_names()
        print(f"Created tables: {tables}")
        
        if 'blacklist_entries' in tables:
            print("✓ blacklist_entries table created")
        else:
            print("✗ blacklist_entries table not found")

def drop_database():
    """Drop all database tables"""
    app = create_app()
    
    with app.app_context():
        print("Dropping all database tables...")
        db.drop_all()
        print("All tables dropped successfully!")

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Database management for blacklist microservice')
    parser.add_argument('action', choices=['init', 'drop'], help='Action to perform')
    
    args = parser.parse_args()
    
    if args.action == 'init':
        init_database()
    elif args.action == 'drop':
        drop_database()

if __name__ == "__main__":
    main()
