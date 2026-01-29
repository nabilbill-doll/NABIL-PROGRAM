import requests

URL = "http://127.0.0.1:5000/barang"

def tambah_barang():
    nama = input("Nama barang: ")
    jumlah = input("Jumlah: ")
    data = {"nama": nama, "jumlah": jumlah}
    requests.post(URL, json=data)
    print("Data berhasil dikirim\n")

def lihat_barang():
    response = requests.get(URL)
    for i, barang in enumerate(response.json()):
        print(f"{i+1}. {barang['nama']} - Stok: {barang['jumlah']}")
    print()

while True:
    print("=== CLIENT INVENTORY ===")
    print("1. Tambah Barang")
    print("2. Lihat Barang")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_barang()
    elif pilihan == "2":
        lihat_barang()
    elif pilihan == "3":
        break
    else:
        print("Menu tidak tersedia\n")
