import psycopg2
import os

# Pega aquí tu DATABASE_URL de Railway
DATABASE_URL = "postgresql://postgres:TXjyAwjXdMMvFHXjNLsiQzMpwRMoVWlh@shinkansen.proxy.rlwy.net:23755/railway"

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Conexión exitosa a Railway PostgreSQL")
    conn.close()
except Exception as e:
    print(f"Error: {e}")
