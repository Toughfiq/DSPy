import pandas as pd

# Mengatur tampilan jumlah kolom maksimal menjadi 15
pd.set_option("display.max_columns", 15)

'''
Start DS and visualize the dataset
'''
try:
    # Gunakan raw string (r"...") atau double backslash (\\) untuk menghindari Unicode escape error
    file_path = r"C:\Users\user\Downloads\DataRole\DSPy\Soybean.csv"
    
    # Membaca dataset
    table = pd.read_csv(file_path)

    # Menampilkan 5 baris pertama
    print(table.head())
    # Menampilkan jumlah data kosong
    print(table.isna().sum())
    '''
    menampilkan summary dari data seperti di Bahasa R menggunakan print(dataSetName.describe())
    sementara yang dibawah ini digunakan untuk menapilkan ringkasan semua tipe data
    '''
    print(table.describe(include="all"))
    # Menampilkan informasi dataset, termasuk tipe data, ukuran, dan jumlah data kosong
    print(table.info())
    

except FileNotFoundError:
    print("Error: File tidak ditemukan. Pastikan path benar.")

except Exception as e:
    print(f"Terjadi error: {e}")
