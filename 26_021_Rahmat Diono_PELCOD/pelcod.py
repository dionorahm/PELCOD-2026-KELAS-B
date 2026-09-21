Nama = "Rahmat Diono"
umur = 18
tinggi = 165
angka_favorit = -20002

print("nama :", Nama)
print("umur :", umur)
print("tinggi :", tinggi)
print("angka favorit :", angka_favorit)
print("\n")

harga_pensil = 2000
jumlah_pensil = 4
harga_buku = 5000
jumlah_buku = 2

print(f"harga pensil: Rp{harga_pensil}")
print(f"jumlah pensil:",jumlah_pensil,"buah")
print(f"harga buku: Rp{harga_buku}")
print("jumlah buku:",jumlah_buku,"pcs")
total_pensil = harga_pensil*jumlah_pensil
total_buku = harga_buku*jumlah_buku
print("total harga pensil :", harga_pensil, "x", jumlah_pensil, "=", total_pensil)
print("total harga buku :", harga_buku, "x", jumlah_buku, "=", total_buku)
harga_total = total_pensil + total_buku
print(f"harga totalnya jadi Rp{harga_total}")


if angka_favorit %2 == 0:
    print(f"{angka_favorit} adalah angka genap")
else:
    print(f"{angka_favorit} adalah angka ganjil")