#Flake8 kombinuje Pyflakes, pycodestyle (PEP 8) a McCabe (komplexnosť). Tu je príklad, ktorý odhalí niektoré z jeho detekcií:
def dlha_funkcia(a, b, c, d, e, f, g, h, i, j):
    # Chyba: Príliš dlhý riadok (PEP 8)
    return a + b + c + d + e + f + g + h + i + j

def funkcia_s_komplexnou_logikou(x):
    # Chyba: Príliš vysoká cyklomatická komplexnosť (McCabe)
    if x > 10:
        if x % 2 == 0:
            if x > 20:
                if x % 3 == 0:
                    return "A"
                else:
                    return "B"
            else:
                return "C"
        else:
            return "D"
    else:
        return "E"

vysledok1 = dlha_funkcia(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
vysledok2 = funkcia_s_komplexnou_logikou(15)

print(vysledok1, vysledok2)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for cislo in dlhy_zoznam:
    if cislo > 5:
        print(funkcia_s_komplexnou_logikou(cislo))

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