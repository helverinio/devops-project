from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from app import db
from app.models.blacklist import BlacklistEntry
from app.schemas.blacklist import (
    BlacklistEntrySchema, 
    BlacklistResponseSchema, 
    BlacklistCheckResponseSchema
)

class BlacklistResource(Resource):
    @jwt_required()
    def post(self):
        """Add an email to the global blacklist"""
        try:
            json_data = request.get_json()
            if not json_data:
                return {'message': 'No input data provided'}, 400
            
            schema = BlacklistEntrySchema()
            validated_data = schema.load(json_data)
            
            client_ip = request.environ.get('HTTP_X_FORWARDED_FOR', 
                                         request.environ.get('REMOTE_ADDR', '127.0.0.1'))
            
            existing_entry = BlacklistEntry.query.filter_by(email=validated_data['email']).first()
            if existing_entry:
                return {
                    'message': 'Email is already in the blacklist',
                    'email': validated_data['email']
                }, 409
            
            blacklist_entry = BlacklistEntry(
                email=validated_data['email'],
                app_uuid=validated_data['app_uuid'],
                blocked_reason=validated_data.get('blocked_reason'),
                ip_address=client_ip
            )
            
            db.session.add(blacklist_entry)
            db.session.commit()
            
            response_schema = BlacklistResponseSchema()
            return response_schema.dump({
                'message': 'Email successfully added to blacklist',
                'email': blacklist_entry.email,
                'created_at': blacklist_entry.created_at
            }), 201
            
        except ValidationError as err:
            return {'message': 'Validation error', 'errors': err.messages}, 400
        except IntegrityError:
            db.session.rollback()
            return {'message': 'Email is already in the blacklist'}, 409
        except Exception as e:
            db.session.rollback()
            return {'message': 'Internal server error'}, 500

class BlacklistCheckResource(Resource):
    @jwt_required()
    def get(self, email):
        """Check if an email is in the global blacklist"""
        try:
            from app.schemas.blacklist import validate_email_format
            validate_email_format(email)
            
            blacklist_entry = BlacklistEntry.query.filter_by(email=email).first()
            
            response_data = {
                'email': email,
                'is_blacklisted': blacklist_entry is not None,
                'blocked_reason': blacklist_entry.blocked_reason if blacklist_entry else None,
                'created_at': blacklist_entry.created_at if blacklist_entry else None
            }
            
            response_schema = BlacklistCheckResponseSchema()
            return response_schema.dump(response_data), 200
            
        except ValidationError as err:
            return {'message': 'Invalid email format', 'errors': err.messages}, 400
        except Exception as e:
            return {'message': 'Internal server error'}, 500
