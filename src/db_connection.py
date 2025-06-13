import cx_Oracle

def get_connection():
    dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XE")  # Replace XE if yours is different
    conn = cx_Oracle.connect(user="system", password="admin", dsn=dsn)
    return conn
