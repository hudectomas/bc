# Neefektívne logické výrazy - opravená verzia

def check_conditions(a, b, c):
    # Optimalizovaná kontrola boolean hodnoty
    if a:
        print("a je True")

    # Odstránená duplicitná podmienka
    if b > 0:
        print("b je kladné číslo")

    # Eliminované zbytočné porovnanie s None
    if c is not None:
        print("c nie je None")

    # Priama kontrola bez neefektívnej negácie
    if a:
        print("a nie je False")

    # Odstránená nadbytočná kontrola
    print("Táto podmienka je vždy True") if a else None


def redundant_logic(x, y):
    # Odstránené duplicitné logické výrazy
    if x:
        print("x je pravdivé")

    # Priama logická operácia
    if y:
        print("y je pravdivé")

    # Zredukované podmienky na jasné vetvenie
    if x:
        print("x je pravda")
    else:
        print("x je nepravda")

    # Odstránené duplicitné porovnanie
    if y == 5:
        print("y je 5")

    # Priama návratová hodnota bez nadbytočnej podmienky
    return x


def main():
    # Testovanie opravených logických výrazov
    check_conditions(True, 10, None)
    redundant_logic(False, 5)

if __name__ == "__main__":
    main()
