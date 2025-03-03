def je_parne(cislo):
    return cislo % 2 == 0

def je_kladne_a_parne(cislo):
    return cislo > 0 and je_parne(cislo)

if je_parne(4):
    print("4 je párne")

if je_kladne_a_parne(6):
    print("6 je kladné a párne")

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for cislo in dlhy_zoznam:
    if je_parne(cislo):
        print(cislo)