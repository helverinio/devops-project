from flask import request
from flask_restful import Resource
from app.utils.auth import generate_token

class AuthResource(Resource):
    def post(self):
        """Generate JWT token for authentication"""
        json_data = request.get_json()
        
        # Simple authentication - in production, validate against user database
        if not json_data or not json_data.get('client_id'):
            return {'message': 'Client ID is required'}, 400
        
        client_id = json_data['client_id']
        
        # Generate token
        token = generate_token(identity=client_id)
        
        return {
            'access_token': token,
            'token_type': 'Bearer',
            'expires_in': 86400  # 24 hours in seconds
        }, 200
