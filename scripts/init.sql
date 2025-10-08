-- Initialize the blacklist database with proper indexes and constraints

-- Create the blacklist_entries table if it doesn't exist
CREATE TABLE IF NOT EXISTS blacklist_entries (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    app_uuid VARCHAR(36) NOT NULL,
    blocked_reason VARCHAR(255),
    ip_address VARCHAR(45) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_blacklist_email ON blacklist_entries(email);
CREATE INDEX IF NOT EXISTS idx_blacklist_created_at ON blacklist_entries(created_at);
CREATE INDEX IF NOT EXISTS idx_blacklist_app_uuid ON blacklist_entries(app_uuid);

-- Add comments for documentation
COMMENT ON TABLE blacklist_entries IS 'Global email blacklist entries';
COMMENT ON COLUMN blacklist_entries.email IS 'Email address to be blacklisted';
COMMENT ON COLUMN blacklist_entries.app_uuid IS 'UUID of the application that added this entry';
COMMENT ON COLUMN blacklist_entries.blocked_reason IS 'Optional reason for blacklisting';
COMMENT ON COLUMN blacklist_entries.ip_address IS 'IP address from which the request was made';
COMMENT ON COLUMN blacklist_entries.created_at IS 'Timestamp when the entry was created';
