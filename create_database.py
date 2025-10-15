#!/usr/bin/env python3
"""
Script para crear la base de datos blacklist_db en RDS
"""
import psycopg
import sys
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

database_url = os.environ.get('DATABASE_URL')
print(f"Connecting to: {database_url}")

try:
    # Extraer componentes de la URL
    url_parts = database_url.replace('postgresql+psycopg://', '').split('/')
    host_part = url_parts[0]
    current_db = url_parts[1]   # postgres
    
    # Separar credenciales y host
    user_pass, host_port = host_part.split('@')
    user, password = user_pass.split(':')
    host, port = host_port.split(':')
    
    print(f"Connecting to {host}:{port} as {user} to database '{current_db}'")
    
    # Conectar a la base de datos postgres (por defecto)
    conn = psycopg.connect(
        host=host,
        port=int(port),
        user=user,
        password=password,
        dbname=current_db,  # postgres
        connect_timeout=10
    )
    
    # Configurar autocommit para poder crear base de datos
    conn.autocommit = True
    
    print("✅ Connected successfully to postgres database")
    
    with conn.cursor() as cur:
        # Verificar si la base de datos ya existe
        cur.execute("SELECT 1 FROM pg_database WHERE datname = 'blacklist_db';")
        exists = cur.fetchone()
        
        if exists:
            print("✅ Database 'blacklist_db' already exists")
        else:
            # Crear la base de datos
            print("Creating database 'blacklist_db'...")
            cur.execute("CREATE DATABASE blacklist_db;")
            print("✅ Database 'blacklist_db' created successfully")
    
    conn.close()
    print("✅ Connection closed")
    
    # Ahora actualizar el .env para usar blacklist_db
    print("\nUpdating .env file to use blacklist_db...")
    
except Exception as e:
    print(f"❌ Error: {type(e).__name__}: {e}")
    sys.exit(1)