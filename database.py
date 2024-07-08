import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect('condo.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            profile TEXT,
            email TEXT,
            condo_id INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS condos (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS financial (
            id INTEGER PRIMARY KEY,
            condo_id INTEGER,
            date TEXT,
            description TEXT,
            amount REAL,
            type TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY,
            condo_id INTEGER,
            item_name TEXT,
            quantity INTEGER,
            date_added TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY,
            condo_id INTEGER,
            resident_id INTEGER,
            amount REAL,
            payment_date TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS providers (
            id INTEGER PRIMARY KEY,
            condo_id INTEGER,
            provider_name TEXT,
            service TEXT,
            contact_info TEXT
        )
    ''')
    conn.commit()
    add_admin_user(conn)
    conn.close()

def add_admin_user(conn):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO users (username, password, profile, email, condo_id)
        VALUES (?, ?, ?, ?, ?)
    ''', ('admin', 'admin123', 'ADM', 'admin@example.com', 1))
    conn.commit()

def get_financial_data(condo_id, year):
    conn = sqlite3.connect('condo.db')
    query = """
    SELECT 
        strftime('%m', date) as month,
        SUM(CASE WHEN type = 'receita' THEN amount ELSE 0 END) as receita,
        SUM(CASE WHEN type = 'despesa' THEN amount ELSE 0 END) as despesa
    FROM financial
    WHERE condo_id = ? AND strftime('%Y', date) = ?
    GROUP BY strftime('%m', date)
    """
    df = pd.read_sql_query(query, conn, params=(condo_id, str(year)))
    df['saldo'] = df['receita'] - df['despesa']
    conn.close()
    return df

if __name__ == "__main__":
    init_db()
