from datetime import datetime, timezone
from app import db

class BlacklistEntry(db.Model):
    __tablename__ = 'blacklist_entries'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True, index=True)
    app_uuid = db.Column(db.String(36), nullable=False)
    blocked_reason = db.Column(db.String(255), nullable=True)
    ip_address = db.Column(db.String(45), nullable=False)  # Supports both IPv4 and IPv6
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f'<BlacklistEntry {self.email}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'app_uuid': self.app_uuid,
            'blocked_reason': self.blocked_reason,
            'ip_address': self.ip_address,
            'created_at': self.created_at.isoformat()
        }
