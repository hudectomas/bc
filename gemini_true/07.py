import sys

def faktorial(n):
    if n > sys.getrecursionlimit() -1:
        return float('inf')
    vysledok = 1
    for i in range(1, n + 1):
        vysledok *= i
    return vysledok

vysledok1 = faktorial(20)
vysledok2 = faktorial(15)

print(vysledok1, vysledok2)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for cislo in dlhy_zoznam:
    print(faktorial(cislo))