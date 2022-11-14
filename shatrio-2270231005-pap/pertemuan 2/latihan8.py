#konversi suhu temperature

print('\nPROGRAM KONVERSI TEMPERATURE\n')

print('===CELCIUS CONVERT KE REANUR,FAHRENHEIT DAN KELVIN===')
celcius = float(input('Masukan suhu dalam celcius yg akan terconvert ngab :'))
print('Suhunya adalah',celcius,'celcius')

# reamur
print('===REAMUR===')
reamur = (4/5) * celcius
print("suhu dalam reamurnya",reamur, "Reamur")

# fahrenheit
print('===FAHRENHEIT===')
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheitnya",fahrenheit, "Fahrenheit")

# Kelvin
print('===KELVIN===')
kelvin = celcius + 273
print("suhu dalam kelvinya ",kelvin, "Kelvin")