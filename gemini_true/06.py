def delenie(a, b):
    if b == 0:
        return None  # Alebo iná vhodná hodnota
    return a / b

vysledok1 = delenie(10, 2)
vysledok2 = delenie(5, 1)

print(vysledok1, vysledok2)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for cislo in dlhy_zoznam:
    if cislo != 0:
        print(delenie(10, cislo))