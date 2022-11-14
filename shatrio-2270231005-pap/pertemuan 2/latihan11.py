
#Latihan Komparasi dan Logika
# membuat gabungan area rentang dari angka

# ++++++3--------10+++++++
inputUser = float(input("masukan angka yang bernilai \nkurang dari 3 atau lebih besar dari 10\n:"))
# ++++++3-----------------
# Memeriksa angka kurang dari 3
isikurangdari = (inputUser < 3)
print("Kurang dari 3 =", isikurangdari)

#----------10++++++
#memeriksa angka lebih dari 10
isilebihdari = (inputUser > 10)
print('masuka angka lebih dari 10 =',isikurangdari)


# ++++++3--------10+++++++

isicorect = isikurangdari or isilebihdari
print('angka yg dimasukan',isicorect)

# -----3++++++++10--------
# kasus irisan
print("\n",10*"=","\n")
inputUser = float(input("masukan angka yang bernilai\nlebih dari 3 dan\nkurang dari 10:"))

# -----3++++++++++++++++++
# lebih dari 3isLebihDari = inputUser > 3

print("Lebih dari 3 = ",isilebihdari)
# +++++++++++++++10-------
# kurang dari 10
isikurangdari = inputUser < 10
print("Kurang dari 10 = ",isikurangdari)

# -----3++++++++10--------
isicorrect = isikurangdari and isilebihdari
print("angka yang anda masukan: ", isicorrect)