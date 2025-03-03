def sucet(a: int, b: int) -> int:
    return a + b

def vypocitaj_priemer(zoznam: list[int]) -> float:
    if not zoznam:
        return 0.0
    return sum(zoznam) / len(zoznam)

vysledok1 = sucet(1, 2)
zoznam = [1, 2, 3, 4, 5]
priemer = vypocitaj_priemer(zoznam)

print(vysledok1, priemer)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
vysledky = []
for prvok in dlhy_zoznam:
    vysledky.append(sucet(prvok, 1))

for vysledok in vysledky:
    print(vysledok)