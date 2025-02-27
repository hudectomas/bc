def rekurzivna_funkcia(n):
    if n > 0:
        return rekurzivna_funkcia(n)
    else:
        return 0

# Chyba: Nekonečná rekurzia
vysledok1 = rekurzivna_funkcia(10)

# Chyba: Nekonečná rekurzia
vysledok2 = rekurzivna_funkcia(5)

print(vysledok1, vysledok2)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for cislo in dlhy_zoznam:
    print(rekurzivna_funkcia(cislo))

# Zbytočný kód
s = 80