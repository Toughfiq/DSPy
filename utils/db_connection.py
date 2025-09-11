import mysql.connector
import pandas as pd

# Buat koneksi ke database
def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Databases123',
        database='DatingSQL'
    )

# Fungsi untuk mengambil banyak kolom dari tabel
def load_columns(column_names, table='user_data'):
    try:
        if not isinstance(column_names, list):
            raise ValueError("Parameter column_names harus berupa list.")

        conn = get_connection()
        columns = ", ".join([f"`{col}`" for col in column_names])
        query = f"SELECT {columns} FROM {table}"
        df = pd.read_sql_query(query, conn)
        return df

    except (mysql.connector.Error, ValueError) as err:
        print(f"[LoadColumns Error] {err}")
        return pd.DataFrame()
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()

# Fungsi untuk mengambil satu kolom (alias)
def load_column(column_name, table='user_data'):
    try:
        return load_columns([column_name], table)
    except Exception as e:
        print(f"[LoadColumn Error] {e}")
        return pd.DataFrame()

