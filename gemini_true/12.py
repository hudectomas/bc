def vypocitaj_priemer(zoznam):
    if not zoznam:
        return 0
    return sum(zoznam) / len(zoznam)

def dlha_funkcia(a, b, c, d, e, f, g, h, i, j):
    return a + b + c + d + e + f + g + h + i + j

vysledok1 = dlha_funkcia(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def funkcia_s_premennymi():
    premenne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    return sum(premenne)

vysledok2 = funkcia_s_premennymi()

print(vysledok1, vysledok2)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
priemer = vypocitaj_priemer(dlhy_zoznam)
print(priemer)