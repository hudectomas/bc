import math
import random
import os

def vypocitaj_sinus(x):
    return math.sin(x)

def generuj_nahodne_cislo():
    return random.randint(1, 100)

# Chyba: Nepoužitý import 'os'

vysledok_sinus = vypocitaj_sinus(math.pi / 2)
nahodne_cislo = generuj_nahodne_cislo()

# Chyba: Chýbajúci import 'datetime'
# dnes = datetime.datetime.now()

print(vysledok_sinus)
print(nahodne_cislo)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for cislo in dlhy_zoznam:
    print(math.cos(cislo))

# Zbytočný kód
a = 10
b = 20
c = 30
d = 40
e = 50
f = 60
g = 70
h = 80
i = 90
j = 100