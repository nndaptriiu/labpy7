## Nama : Ananda Eka Delima Putri
## NIM : 312510210
## Kelas : TI.25.A.2
## Pertemuan : 12

## Input kode praktikum 7

<img width="1756" height="786" alt="Screenshot 2025-12-04 090941" src="https://github.com/user-attachments/assets/334d6c24-8f9b-411f-b896-b93f0eb95f32" />

## Output kode praktikum 7

<img width="1494" height="644" alt="Screenshot 2025-12-04 090957" src="https://github.com/user-attachments/assets/bce1eb67-ca7c-4019-bf48-442e7bc57551" />

## flowchart
```
               ┌───────────────┐
               │     Mulai     │
               └───────┬───────┘
                       │
               ┌───────▼────────┐
               │  Buat Object   │
               │ NilaiMahasiswa │
               └───────┬────────┘
                       │
             ┌─────────▼──────────┐
             │    tambah()        │
             └─────────┬──────────┘
                       │
             ┌─────────▼──────────┐
             │   tampilkan()      │
             └─────────┬──────────┘
                       │
             ┌─────────▼──────────┐
             │      ubah()        │
             └─────────┬──────────┘
                       │
             ┌─────────▼──────────┐
             │    tampilkan()     │
             └─────────┬──────────┘
                       │
             ┌─────────▼──────────┐
             │     hapus()        │
             └─────────┬──────────┘
                       │
             ┌─────────▼──────────┐
             │    tampilkan()     │
             └─────────┬──────────┘
                       │
                  ┌────▼────┐
                  │ Selesai │
                  └─────────┘
```
## DIAGRAM CLASS (UML)
```
+--------------------------------+
|        NilaiMahasiswa          |
+--------------------------------+
| - data : dict                  |
+--------------------------------+
| + tambah(nama, nilai)          |
| + tampilkan()                  |
| + hapus(nama)                  |
| + ubah(nama, nilai_baru)       |
+--------------------------------+
```
Keterangan:

data → dictionary penyimpanan (nama → nilai)

tambah() → menambah data

tampilkan() → menampilkan data

hapus() → menghapus data

ubah() → mengubah nilai mahasiswa

## Penjelasan README.md

## Praktikum 8 – Program Daftar Nilai Mahasiswa (OOP)

Program ini dibuat untuk memenuhi tugas Praktikum 8 dengan menerapkan konsep **Object-Oriented Programming (OOP)** dalam bahasa Python.  
Program menggunakan sebuah class bernama `NilaiMahasiswa` yang berfungsi untuk mengelola data nilai mahasiswa.

---

## Tujuan Program
- Mengaplikasikan pemrograman berbasis objek (OOP)
- Menggunakan class, atribut, dan method
- Melakukan operasi tambah, tampilkan, hapus, dan ubah data mahasiswa

---

## Fitur Program

### 1. `tambah(nama, nilai)`
Menambahkan data mahasiswa baru ke dalam dictionary.

### 2. `tampilkan()`
Menampilkan semua data mahasiswa.  
Jika belum ada data, akan muncul pesan: **"Belum ada data."**

### 3. `hapus(nama)`
Menghapus data berdasarkan nama mahasiswa.  
Jika nama tidak ditemukan, tampil pesan error.

### 4. `ubah(nama, nilai_baru)`
Mengubah nilai mahasiswa.  
Jika nama tidak ada dalam data, tampil pesan error.

---


---

## 📘 Penjelasan Program

Program ini menggunakan konsep dasar OOP:

### ✔ **Class**
`NilaiMahasiswa` digunakan untuk menyimpan dan mengelola data mahasiswa.

### ✔ **Atribut**
- `self.data` → dictionary yang menyimpan pasangan (nama: nilai)

### ✔ **Method**
- `tambah()` → memasukkan data baru
- `tampilkan()` → menampilkan seluruh data
- `hapus()` → menghapus data berdasarkan kunci
- `ubah()` → memperbarui nilai mahasiswa






