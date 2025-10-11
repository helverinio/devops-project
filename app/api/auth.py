import logging
from flask import request
from flask_restful import Resource
from app.utils.auth import generate_token

logger = logging.getLogger(__name__)

class AuthResource(Resource):
    def post(self):
        """Generate JWT token for authentication"""
        logger.info("Received token generation request")
        json_data = request.get_json()
        
        # Simple authentication - in production, validate against user database
        if not json_data or not json_data.get('client_id'):
            logger.warning("Token request missing client_id")
            return {'message': 'Client ID is required'}, 400
        
        client_id = json_data['client_id']
        logger.info(f"Generating token for client: {client_id}")

        token = generate_token(identity=client_id)
        logger.info(f"Token generated successfully for client: {client_id}")
        
        return {
            'access_token': token,
            'token_type': 'Bearer',
            'expires_in': 86400  # 24 hours in seconds
        }, 200
