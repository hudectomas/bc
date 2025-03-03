def vypocitaj_priemer(zoznam):
    if not zoznam:
        return 0
    return sum(zoznam) / len(zoznam)

definovana_premenna = 10
vysledok = vypocitaj_priemer([1, 2, 3, 4, 5])

print(definovana_premenna)
print(vysledok)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
priemer = vypocitaj_priemer(dlhy_zoznam)
print(priemer)