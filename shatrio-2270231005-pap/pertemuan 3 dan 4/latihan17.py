
# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5
format_string = f"harga total = Rp. {harga*jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)
print('\n')

print('4. Format String Width and Alignment')

# Data
data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# string standard
data_string = f'nama ={data_nama},umur = {data_umur},tinggi ={data_tinggi},sepatu ={data_nomor_sepatu}'
print(5*"="+"Data String"+5*"=")
print(data_string)

# String multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama},\numur = {data_umur},tinggi =(data_tinggi),sepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# String multiline (kutip triplets)
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar
data_nama = "Ucup Surucup"
data_tinggi = 105.17
data_string = f"""
nama = {data_nama:>5}
umur = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

print('Date and Time (Latihan)')

import datetime as dt

print('Silahkan masukan tanggal,\nbulan dan tahun lahir anda\n')
tanggal = int(input('Tanggal :\t'))
bulan   = int(input('Bulan : \t'))
tahun   = int(input('Tahun : \t'))
tanggal_lahir = dt.date(tahun,bulan,tanggal)

print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
hari_ini = dt.date.today()
umur_hari = hari_ini- tanggal_lahir
umur_tahun = umur_hari.days// 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f"Hari nya adalah : {tanggal_lahir:%A}")
print(f"Umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa}bulan")
print('\n')

print('====If dan Else Statement====')

#  if nya
nama = input("Siapa nama anda? ")
# program sebelumnya
# if kondisi: aksi
# program selanjutnya

# 1. program if inline
# if nama=="ucup" : print("Kamu Ganteng abieeez!!!!")
# print(f"Terima kasih {nama}")


#  kondisinya
# 2.program if indentation
# if nama=="ucup":
# print("kamu ganteng abieeeez!")
# print("kamu juga keren banget!")
# print(f"Terima kasih {nama}")

# aksinya
# 3. Else Statement
if nama=="otong":print("hai otooong, si keren!!!")
else:print("Ah kamu bukan otong, kamu gak keren! :")
print("akhir dari program")
print('\n')


print('====elif statement===')

nama = input("Nama kamyu siapa? ")
if nama == "rio": # kondisi 1
    print("Hai ganteeeeng beuds!") # aksi true 1
elif nama == "indra": # kondisi 2
    print("woyyy kerjaaa!!!") # aksi true 2
elif nama == "dono": # kondisi 3
    print("GILA LU DONN!") # aksi true 3
else:
    print("au ah gak kenal!!!") # aksi false
print("ini adalah akhir dari program")
print('\n\n')


