def rekurzivna_funkcia(n):
    if n > 0:
        return n + rekurzivna_funkcia(n - 1)
    else:
        return 0

vysledok1 = rekurzivna_funkcia(10)
vysledok2 = rekurzivna_funkcia(5)

print(vysledok1, vysledok2)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for cislo in dlhy_zoznam:
    print(rekurzivna_funkcia(cislo))