import csv
import mysql.connector
#file ini akan menginput file csv ke MySQL
# Konfigurasi database
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Databases123',
    'database': 'DatingSQL'
}

csv_file_path = 'DatingBehave.csv'
table_name = 'user_data'# nama tabel SQL
batch_size = 5000 # Jumlah baris yang akan dimasukkan dalam satu transaksi

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Asumsi kolom di CSV cocok dengan kolom di tabel MySQL
    # Anda perlu menyesuaikan ini jika ada perbedaan
    # Contoh: ('kolom1', 'kolom2', 'kolom3')
    # Pastikan urutan kolom sesuai dengan file CSV Anda
    columns = "(" \
    "gender, sexual_orientation," \
    " location_type, income_bracket, education_level," \
    " interest_tags, app_usage_time_min, app_usage_time_label," \
    " swipe_right_ratio, swipe_right_label, likes_received," \
    " mutual_matches, profile_pics_count, bio_length, " \
    "message_sent_count, emoji_usage_rate, last_active_hour," \
    " swipe_time_of_day, match_outcome)" # Ganti dengan nama kolom aktual Anda
    placeholders = "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)" # Sesuaikan jumlah %s dengan jumlah kolom

    insert_query = f"INSERT INTO {table_name} {columns} VALUES {placeholders}"

    data_to_insert = []
    with open(csv_file_path, 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader) # Lewati header

        for i, row in enumerate(csv_reader):
            data_to_insert.append(tuple(row)) # Ubah list menjadi tuple
            if (i + 1) % batch_size == 0:
                cursor.executemany(insert_query, data_to_insert)
                conn.commit()
                data_to_insert = []
                print(f"Inserted {i + 1} rows...")

        # Masukkan sisa data jika ada
        if data_to_insert:
            cursor.executemany(insert_query, data_to_insert)
            conn.commit()
            print(f"Finished inserting all rows. Total: {i + 1}")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()