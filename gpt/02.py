# Neefektívne logické výrazy - dlhší program s viacerými chybami

def check_conditions(a, b, c):
    # Chyba 1: Zbytočná podmienka
    if a == True:
        print("a je True")

    # Chyba 2: Duplicitné kontroly
    if b > 0 or b > 0:
        print("b je kladné číslo")

    # Chyba 3: Zbytočné porovnanie s None
    if c is not None:
        if c is not None:
            print("c nie je None")

    # Chyba 4: Neefektívna negácia
    if not (a == False):
        print("a nie je False")

    # Chyba 5: Nadbytočná kontrola
    if a or True:
        print("Táto podmienka je vždy True")


def redundant_logic(x, y):
    # Chyba 6: Neefektívna podmienka
    if x and x:
        print("x je pravdivé")

    # Chyba 7: Zbytočná logická operácia
    if (y and True) or False:
        print("y je pravdivé")

    # Chyba 8: Redundantné vetvy
    if x:
        print("x je pravda")
    else:
        if not x:
            print("x je nepravda")

    # Chyba 9: Opakované porovnanie
    if y == 5 or y == 5:
        print("y je 5")

    # Chyba 10: Zbytočný návrat
    if x:
        return True
    else:
        return False


def main():
    # Testovanie neefektívnych logických výrazov
    check_conditions(True, 10, None)
    redundant_logic(False, 5)

if __name__ == "__main__":
    main()
