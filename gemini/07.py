def faktorial(n):
    vysledok = 1
    for i in range(1, n + 1):
        vysledok *= i
    return vysledok

# Chyba: Pretečenie premennej (pre veľké n)
vysledok1 = faktorial(1000)

# Chyba: Pretečenie premennej (pre veľké n)
vysledok2 = faktorial(2000)

print(vysledok1, vysledok2)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for cislo in dlhy_zoznam:
    print(faktorial(cislo * 100))

# Zbytočný kód
t = 70