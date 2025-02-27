#Mypy je statický typový kontrolór. Tu je príklad, ktorý odhalí niektoré z jeho detekcií:
def sucet(a: int, b: int) -> int:
    return a + b

def vypocitaj_priemer(zoznam: list[int]) -> float:
    return sum(zoznam) / len(zoznam)

# Chyba: Nekonzistentný typ argumentu (očakávaný int, dostal str)
vysledok1 = sucet(1, "2")

# Chyba: Nekonzistentný typ prvku v zozname (očakávaný int, dostal str)
zoznam = [1, 2, 3, "4", 5]
priemer = vypocitaj_priemer(zoznam)

print(vysledok1, priemer)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
vysledky = []
for prvok in dlhy_zoznam:
    vysledky.append(sucet(prvok, 1))

for vysledok in vysledky:
    print(vysledok)

# Zbytočný kód
u = 10
v = 20
w = 30
x = 40
y = 50
z = 60
aa = 70
bb = 80
cc = 90
dd = 100