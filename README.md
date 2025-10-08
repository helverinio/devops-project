# Email Blacklist Microservice

A Flask-based microservice for managing a global email blacklist system. This service allows multiple internal systems to check if an email is blacklisted and add emails to the global blacklist.


## Quick Start with Docker Compose (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd devops-test
   ```

2. **Start the services**
   ```bash
   docker-compose up -d
   ```

3. **Verify services are running**
   ```bash
   docker-compose ps
   ```

4. **Check application logs**
   ```bash
   docker-compose logs -f blacklist-api
   ```

The API will be available at `http://localhost:5000`
PostgreSQL will be available at `localhost:5432`

### Stop Services
```bash
docker-compose down
```

## Docker Deployment

### Using Docker Compose (Recommended)

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up -d
   ```

2. **Check logs**
   ```bash
   docker-compose logs -f blacklist-api
   ```

3. **Stop services**
   ```bash
   docker-compose down
   ```

## Testing

### Unit Tests
```bash
# Run all tests
python -m pytest tests/ -v

# Run simple test
python tests/test_api.py
```

