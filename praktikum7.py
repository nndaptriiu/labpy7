class NilaiMahasiswa:
    def __init__(self):
        self.data = {}   # key = nama, value = nilai

    def tambah(self, nama, nilai):
        self.data[nama] = nilai
        print(f"Data '{nama}' berhasil ditambahkan.")

    def tampilkan(self):
        if not self.data:
            print("Belum ada data.")
        else:
            print("\nDaftar Nilai Mahasiswa:")
            for nama, nilai in self.data.items():
                print(f"- {nama}: {nilai}")

    def hapus(self, nama):
        if nama in self.data:
            del self.data[nama]
            print(f"Data '{nama}' berhasil dihapus.")
        else:
            print(f"Data '{nama}' tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        if nama in self.data:
            self.data[nama] = nilai_baru
            print(f"Data '{nama}' berhasil diubah.")
        else:
            print(f"Data '{nama}' tidak ditemukan.")


# Contoh penggunaan
if __name__ == "__main__":
    nm = NilaiMahasiswa()
    nm.tambah("Aisyah", 90)
    nm.tampilkan()
    nm.ubah("Aisyah", 95)
    nm.tampilkan()
    nm.hapus("Aisyah")
    nm.tampilkan()
