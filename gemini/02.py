def je_parne(cislo):
    if cislo % 2 == 0:
        return True
    else:
        return False

def je_kladne_a_parne(cislo):
    if cislo > 0:
        if je_parne(cislo):
            return True
        else:
            return False
    else:
        return False

# Neefektívne: Zbytočné porovnanie s True
if je_parne(4) == True:
    print("4 je párne")

# Neefektívne: Zbytočné vnorené if-else
if je_kladne_a_parne(5):
    print("5 je kladné a párne")

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for cislo in dlhy_zoznam:
    if je_parne(cislo):
        print(cislo)

# Zbytočný kód
y = 20