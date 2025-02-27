def delenie(a, b):
    return a / b

# Chyba: Delenie nulou
vysledok1 = delenie(10, 0)

# Chyba: Delenie nulou
vysledok2 = delenie(5, 0)

print(vysledok1, vysledok2)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for cislo in dlhy_zoznam:
    print(delenie(10, cislo - cislo))

# Zbytočný kód
u = 60