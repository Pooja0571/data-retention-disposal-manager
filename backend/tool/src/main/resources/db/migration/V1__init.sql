CREATE TABLE IF NOT EXISTS users (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'USER',
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS data_records (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    data_type VARCHAR(100) NOT NULL,
    owner VARCHAR(100),
    department VARCHAR(100),
    status VARCHAR(50) NOT NULL DEFAULT 'ACTIVE',
    retention_years INTEGER NOT NULL,
    created_date DATE NOT NULL,
    expiry_date DATE,
    ai_description TEXT,
    ai_score DOUBLE PRECISION,
    is_deleted BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_data_records_status ON data_records(status);
CREATE INDEX IF NOT EXISTS idx_data_records_expiry ON data_records(expiry_date);
CREATE INDEX IF NOT EXISTS idx_data_records_is_deleted ON data_records(is_deleted);

CREATE TABLE IF NOT EXISTS audit_logs (
    id BIGSERIAL PRIMARY KEY,
    entity_type VARCHAR(100),
    entity_id BIGINT,
    action VARCHAR(50),
    performed_by VARCHAR(100),
    performed_at TIMESTAMP,
    details TEXT
);
