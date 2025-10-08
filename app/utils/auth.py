from flask_jwt_extended import create_access_token
from datetime import timedelta

def generate_token(identity, expires_delta=None):
    """Generate JWT access token"""
    if expires_delta is None:
        expires_delta = timedelta(hours=24)
    
    return create_access_token(
        identity=identity,
        expires_delta=expires_delta
    )
