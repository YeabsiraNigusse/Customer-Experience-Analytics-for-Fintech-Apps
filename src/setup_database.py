from db_connection import get_connection
import cx_Oracle

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Drop tables if exist (with CASCADE CONSTRAINTS to remove dependencies)
    for table in ['reviews', 'banks']:
        try:
            cursor.execute(f"DROP TABLE {table} CASCADE CONSTRAINTS")
        except cx_Oracle.DatabaseError:
            pass  # Table didn't exist, no problem

    # Create banks table
    cursor.execute("""
        CREATE TABLE banks (
            id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
            name VARCHAR2(100) NOT NULL UNIQUE
        )
    """)

    # Create reviews table
    cursor.execute("""
        CREATE TABLE reviews (
            id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
            bank_id NUMBER NOT NULL REFERENCES banks(id),
            review_text CLOB,
            sentiment VARCHAR2(20),
            theme VARCHAR2(100),
            review_date DATE
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()
