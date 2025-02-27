def sucet(a, b, c):
    return a + b + c

def vypocitaj_priemer(zoznam):
    return sum(zoznam) / len(zoznam)

# Chyba: Príliš málo argumentov
vysledok1 = sucet(1, 2)

# Chyba: Príliš veľa argumentov
vysledok2 = vypocitaj_priemer([1, 2, 3], 0)

print(vysledok1, vysledok2)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
priemer = vypocitaj_priemer(dlhy_zoznam)
print(priemer)

# Zbytočný kód
x = 10