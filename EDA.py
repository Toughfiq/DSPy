import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

#Load data menggunakan database config
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Databases123',
    'database': 'DatingSQL'
}
#Membuat handling exception
try:
    conn = mysql.connector.connect(**db_config)
    
    # Mengubah query untuk mengambil SEMUA kolom
    sql_query = "SELECT * FROM user_data" 
    
    # Menggunakan pd.read_sql_query untuk memuat data langsung ke DataFrame
    data_df = pd.read_sql_query(sql_query, conn) #data_df sudah menjadi sebuah dataframe di pandas
    
    print("All data successfully loaded from MySQL.")

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL or executing query: {err}")
    exit() # Keluar dari skrip jika gagal terhubung ke DB
finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("MySQL connection closed.")
