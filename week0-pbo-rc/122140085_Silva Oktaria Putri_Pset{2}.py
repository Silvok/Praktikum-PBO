nilai_mahasiswa = {}

jumlah_mahasiswa = int(input("Silakan masukkan jumlah mahasiswa: "))

for i in range(jumlah_mahasiswa):
    nama_mahasiswa = input("Nama mahasiswa: ")
    nilai = int(input("Nilai: "))
    
    nilai_mahasiswa[nama_mahasiswa] = nilai

print("Data nilai mahasiswa:", nilai_mahasiswa)5
