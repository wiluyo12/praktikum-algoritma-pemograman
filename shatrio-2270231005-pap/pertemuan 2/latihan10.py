#and = mengembalikan TRUE jika dua statement sama2 benar
#or  = mengembalikan TRUE jika slah satu statement bernilai benar
#not = mengembalikan TRUE menjadi FALSE dan sebalikanya


# NOT
print('\n====NOT====\n')
a = False
c = not a
print('data a =',a)
print('-------------- NOT')
print('data c =',c)

# OR (jika salah satu true, maka hasilnya adalah true)
print('====OR====')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,' =',c)
a = True
b = False
c = a or b
print(a,' OR',b,'=',c)
a = True
b = True
c = a or bprint(a,' OR',b,' =',c)

# AND (jika dua buah nilai true, maka hasil true)
print('====AND====')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = True
b = False
c = a and b
print(a,' AND',b,'=',c)
a = True
b = True
c = a and b
print(a,' AND',b,' =',c)

# XOR (akan true jika salah satu true, sisanya false)
print('====XOR====')
a = False
b = Falsec = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = False
c = a ^ b
print(a,' XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,' XOR',b,' =',c)


