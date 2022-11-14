# data yang dimasukan pasti string

data = input("siapa nama lu?")
print("data = ",data,",type =",type(data))

# jika kita ingin mengambil int, maka
angka_float = float(input("masukan nilai float: "))
angka = int(input("masukan angka: "))
print("data = ",angka_float,",type =",type(angka_float))
print("data = ",angka,",type =",type(angka))

#bagaimana dengan boolean

biner = bool(int(input("masukan nilai boolean.1/0: ")))
print("data = ",biner,",type =",type(biner))