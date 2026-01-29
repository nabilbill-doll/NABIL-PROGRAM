class Barang:
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def __str__(self):
        return f"{self.nama} - Stok: {self.jumlah}"

daftar_barang = []

def tambah_barang():
    nama = input("Nama barang: ")
    jumlah = int(input("Jumlah: "))
    barang = Barang(nama, jumlah)
    daftar_barang.append(barang)
    print("Barang berhasil ditambahkan\n")

def tampilkan_barang():
    if not daftar_barang:
        print("Data barang kosong\n")
    else:
        for i, barang in enumerate(daftar_barang):
            print(f"{i+1}. {barang}")
        print()

def hapus_barang():
    tampilkan_barang()
    index = int(input("Pilih nomor barang yang dihapus: ")) - 1
    if 0 <= index < len(daftar_barang):
        daftar_barang.pop(index)
        print("Barang berhasil dihapus\n")
    else:
        print("Pilihan tidak valid\n")

def menu():
    while True:
        print("=== MENU INVENTORY ===")
        print("1. Tambah Barang")
        print("2. Lihat Barang")
        print("3. Hapus Barang")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            tampilkan_barang()
        elif pilihan == "3":
            hapus_barang()
        elif pilihan == "4":
            print("Terima kasih")
            break
        else:
            print("Menu tidak tersedia\n")

menu()
