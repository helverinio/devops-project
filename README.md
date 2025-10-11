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

Esta aplicación incluye un conjunto completo de tests unitarios que validan toda la funcionalidad de la API.

### Ejecutar Tests con Docker (Recomendado)

```bash
# Ejecutar todos los tests
docker-compose run --rm test

# Ejecutar tests con más verbosidad
docker-compose run --rm test python -m pytest tests/ -v

# Ejecutar un test específico
docker-compose run --rm test python -m pytest tests/test_api.py::BlacklistAPITestCase::test_add_email_to_blacklist -v
```

### Tests Incluidos

Los tests cubren los siguientes escenarios:

1. **Autenticación**
   - ✅ Generación de tokens JWT
   - ✅ Acceso no autorizado

2. **Gestión de Blacklist**
   - ✅ Agregar email a la blacklist
   - ✅ Verificar email en blacklist
   - ✅ Verificar email NO en blacklist
   - ✅ Manejo de emails duplicados

3. **Validaciones**
   - ✅ Formato de email inválido
   - ✅ Formato de UUID inválido

### Resultados Esperados

```
========== test session starts ==========
platform linux -- Python 3.13.8, pytest-7.4.3
collected 8 items

tests/test_api.py::BlacklistAPITestCase::test_add_duplicate_email PASSED     [ 12%]
tests/test_api.py::BlacklistAPITestCase::test_add_email_to_blacklist PASSED  [ 25%]
tests/test_api.py::BlacklistAPITestCase::test_auth_token_generation PASSED   [ 37%]
tests/test_api.py::BlacklistAPITestCase::test_check_blacklisted_email PASSED [ 50%]
tests/test_api.py::BlacklistAPITestCase::test_check_non_blacklisted_email PASSED [ 62%]
tests/test_api.py::BlacklistAPITestCase::test_invalid_email_format PASSED    [ 75%]
tests/test_api.py::BlacklistAPITestCase::test_invalid_uuid_format PASSED     [ 87%]
tests/test_api.py::BlacklistAPITestCase::test_unauthorized_access PASSED     [100%]

========== 8 passed in 1.37s ==========
```

### Usando Makefile

```bash
# Ejecutar tests con pytest
make test

# Ejecutar tests simples con unittest
make test-simple
```

### Ejecutar Tests Localmente (Alternativo)

Si prefieres ejecutar los tests localmente sin Docker:

```bash
# Instalar dependencias
pip install -r requirements.txt
pip install -r requirements-test.txt

# Ejecutar tests
python -m pytest tests/ -v

# O usando unittest
python -m unittest tests.test_api -v
```

### Coverage de Tests

Los tests proporcionan cobertura completa de:
- **API Endpoints**: `/auth/token`, `/blacklists`, `/blacklists/<email>`
- **Validaciones**: Email format, UUID format, autenticación JWT
- **Base de datos**: CRUD operations, manejo de duplicados
- **Manejo de errores**: Responses HTTP apropiados


