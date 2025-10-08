from marshmallow import Schema, fields, validate, ValidationError
from email_validator import validate_email, EmailNotValidError
import uuid

def validate_email_format(email):
    try:
        validate_email(email)
    except EmailNotValidError:
        raise ValidationError('Invalid email format')

def validate_uuid_format(uuid_string):
    try:
        uuid.UUID(uuid_string)
    except ValueError:
        raise ValidationError('Invalid UUID format')

class BlacklistEntrySchema(Schema):
    email = fields.Str(required=True, validate=validate_email_format)
    app_uuid = fields.Str(required=True, validate=validate_uuid_format)
    blocked_reason = fields.Str(validate=validate.Length(max=255), missing=None)

class BlacklistResponseSchema(Schema):
    message = fields.Str()
    email = fields.Str()
    created_at = fields.DateTime()

class BlacklistCheckResponseSchema(Schema):
    email = fields.Str()
    is_blacklisted = fields.Bool()
    blocked_reason = fields.Str(allow_none=True)
    created_at = fields.DateTime(allow_none=True)
