def sucet(a, b):
    return a + b

def vypocitaj_priemer(zoznam):
    return sum(zoznam) / len(zoznam)

# Chyba: Nekonzistentné typy argumentov
vysledok1 = sucet(1, "2")

# Chyba: Nekonzistentné typy premenných
zoznam = [1, 2, 3, "4", 5]
priemer = vypocitaj_priemer(zoznam)

print(vysledok1)
print(priemer)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
vysledky = []
for prvok in dlhy_zoznam:
    vysledky.append(sucet(prvok, "1"))

for vysledok in vysledky:
    print(vysledok)

# Zbytočný kód
k = 10
l = 20
m = 30
n = 40
o = 50
p = 60
q = 70
r = 80
s = 90
t = 100