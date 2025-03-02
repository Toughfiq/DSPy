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

except FileNotFoundError:
    print("Error: File tidak ditemukan. Pastikan path benar.")

except Exception as e:
    print(f"Terjadi error: {e}")
