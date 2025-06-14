import cx_Oracle
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

def get_connection():
    dsn = cx_Oracle.makedsn(
        os.getenv("DB_HOST"),
        os.getenv("DB_PORT"),
        service_name=os.getenv("DB_SERVICE_NAME")
    )
    conn = cx_Oracle.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dsn=dsn
    )
    print("✅ Connection successful!")
    return conn

get_connection()
