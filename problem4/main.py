'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''

harga = int(input("Masukkan Harga (Rp) : "))
disc = int(input("Masukkan diskon (%) : "))
hargaAkhir = int((harga-round((disc*harga/100),2)))
print(f"Harga Setelah Diskon sebesar Rp {hargaAkhir:,}")
