def dlha_funkcia(a, b, c, d, e, f, g, h, i, j):
    return a + b + c + d + e + f + g + h + i + j

def funkcia_s_logikou(x):
    if x > 10:
        if x % 2 == 0:
            return "A"
        else:
            return "B"
    else:
        return "C"

vysledok1 = dlha_funkcia(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
vysledok2 = funkcia_s_logikou(15)

print(vysledok1, vysledok2)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for cislo in dlhy_zoznam:
    if cislo > 5:
        print(funkcia_s_logikou(cislo))