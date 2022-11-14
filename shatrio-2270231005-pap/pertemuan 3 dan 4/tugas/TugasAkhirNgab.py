menu = {
    'ikan cupang'         : 25000,
    'ikan gabus'          : 30000,
    'ikan betok'          : 40000,
    'ikan sepat'          : 30000,
    }
print('=============SELAMAT DATANG DI IKAN HIAS RACING===========\n')
ketik = input('Ketik GAS untuk melanjutkan !!! = ')
if ketik == 'GAS': print('=================OKEE NGABB GASSS===================\n ')
elif ketik == 'gas': print('Aduh salah...TAPI GPP LAHH!!!\n')
else:
    print('Aduhhh salah ngab....TAPI TETEP GAS LAHH\n')

print('=============DAFTAR IKAN YANG TERSEDIA==============')
for i in menu :
    print('Daftar menu :',i,'\tharga = ', menu[i])
print('NOTE = Jika pembelian di atas 50.000,- akan mendapatkan diskon 10%')
print(26*('=='))

nama_pembeli = input('Masukin nama lu ngab = ')
alamat = input('Masukin alamat lu ngab = ')
nomer_telpon = input('Masukin nomer telpon lu ngab = ')
beli = input('Pilih ikan yang mau lu beli ngab = ')
jumlah = int(input('Jumlah pesanan lu ngab = '))
bayar = jumlah*menu[beli]
if bayar > 50000:
    diskon = bayar * 10/100
    total_semua = bayar - diskon
else:
    total_semua = bayar 


print('\n')

print('================PESANAN ATAS NAMA', nama_pembeli,'=====================')
import datetime as dt
hari_ini = dt.datetime.now()
print('Tanggal                        :',hari_ini)
print('Pesanan atas nama ngab         :',nama_pembeli)
print('alamat pembeli                 :',alamat)
print('Ikan yang di beli              :',beli)
print('Total biaya                    :','Rp',bayar)
print('Total yang harus di bayar      :','Rp',total_semua)
print('=============TERIMA KASIH TELAH BERBELANJA NGABB=============')

