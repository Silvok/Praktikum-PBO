import tkinter as tk
from tkinter import messagebox

# Database untuk menyimpan informasi pengguna
basis_data_pengguna = {}

def daftar_pengguna():
    # Mengambil nilai dari input pengguna
    nama_pengguna = entry_nama_pengguna.get()
    kata_sandi = entry_kata_sandi.get()
    konfirmasi_kata_sandi = entry_konfirmasi_kata_sandi.get()

    # Validasi input pengguna
    if not nama_pengguna or not kata_sandi or not konfirmasi_kata_sandi:
        messagebox.showerror("Error", "Harap isi semua kolom.")
        return

    if kata_sandi != konfirmasi_kata_sandi:
        messagebox.showerror("Error", "Kata sandi tidak cocok.")
        return

    if nama_pengguna in basis_data_pengguna:
        messagebox.showerror("Error", "Nama pengguna sudah terdaftar.")
        return

    # Simpan informasi pengguna ke dalam database
    basis_data_pengguna[nama_pengguna] = {'kata_sandi': kata_sandi}
    messagebox.showinfo("Sukses", "Pendaftaran berhasil!")

def tampilkan_jendela_pendaftaran():
    # Membuat jendela pendaftaran baru
    jendela_pendaftaran = tk.Toplevel(root)
    jendela_pendaftaran.title("Pendaftaran Pengguna")

    global entry_nama_pengguna, entry_kata_sandi, entry_konfirmasi_kata_sandi

    # Label dan entry untuk nama pengguna
    tk.Label(jendela_pendaftaran, text="Nama Pengguna:").pack()
    entry_nama_pengguna = tk.Entry(jendela_pendaftaran)
    entry_nama_pengguna.pack()

    # Label dan entry untuk kata sandi
    tk.Label(jendela_pendaftaran, text="Kata Sandi:").pack()
    entry_kata_sandi = tk.Entry(jendela_pendaftaran, show='*')
    entry_kata_sandi.pack()

    # Label dan entry untuk konfirmasi kata sandi
    tk.Label(jendela_pendaftaran, text="Konfirmasi Kata Sandi:").pack()
    entry_konfirmasi_kata_sandi = tk.Entry(jendela_pendaftaran, show='*')
    entry_konfirmasi_kata_sandi.pack()

    # Tombol untuk daftar pengguna
    tk.Button(jendela_pendaftaran, text="Daftar", command=daftar_pengguna).pack()

# Membuat jendela aplikasi utama
root = tk.Tk()
root.title("Aplikasi Pendaftaran Pengguna")

# Label dan tombol untuk membuka jendela pendaftaran
tk.Label(root, text="Selamat Datang!").pack(pady=20)
tk.Button(root, text="Pendaftaran", command=tampilkan_jendela_pendaftaran).pack()

root.mainloop()
