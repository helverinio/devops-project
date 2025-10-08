#!/usr/bin/env python3
"""
Script to generate JWT tokens for testing the blacklist API
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.utils.auth import generate_token

def main():
    app = create_app()
    
    with app.app_context():
        client_id = input("Enter client ID (default: test-client): ") or "test-client"
        token = generate_token(identity=client_id)
        
        print(f"\nGenerated JWT Token for client '{client_id}':")
        print(f"Bearer {token}")
        print(f"\nToken expires in 24 hours")
        print(f"\nUse this token in the Authorization header:")
        print(f"Authorization: Bearer {token}")

if __name__ == "__main__":
    main()
