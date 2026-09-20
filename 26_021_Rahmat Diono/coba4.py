daftar_buku = ["audit","tata kelola","si kancil", "meinkampf", "pemrograman python"]

print("===KOLEKSI BUKU===")
print("0", daftar_buku[0])
print("1", daftar_buku[1])
print("2", daftar_buku[2])
print("3", daftar_buku[3])
print("4", daftar_buku[4])

nama = input("Masukan nama: ")
umur = int(input("Masukan umur: "))
status_aktif = input ("apakah kamu mahasiswa aktif? (y/n)").lower()  == "y"

pilihan1 = int (input("pilih buku kel1 :"))

syarat_umur = status_aktif and umur>=17

hari_sekarang = 0
lama_pinjam = 1
batas_pengembalian = hari_sekarang + lama_pinjam

#\n fungsinya membuat jarak atar print
print("\n===hasil peminjaman===")
if not syarat_umur:
    print(f"maaf {nama}, peminjam ditolak.")
    if not status_aktif:
        print("anda bukan mahasiswa aktif")
else :
    buku_dipinjam = [daftar_buku[pilihan1]]
    print(f"selamat {nama}, peminjam berhasil.")
    print("buku yang dipinjam:", buku_dipinjam)
    print("batas pengembalian:", {batas_pengembalian})