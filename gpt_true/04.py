# Nesprávne použitie znaku rovnosti - opravená verzia

def equality_issues():
    a = 5
    b = 10

    # Opravené porovnanie - '=' nahradené '=='
    if a == b:
        print("a sa rovná b")
    else:
        print("a sa nerovná b")

    # Odstránená zbytočná porovnávacia podmienka
    if a:
        print("a je pravda")

    # Opravené porovnanie rôznych typov
    if str(a) == "5":
        print("a je reťazec '5'")

    # Opravené porovnanie identity
    if a == b:
        print("a a b majú rovnakú hodnotu")

    # Odstránená chybná podmienka s chýbajúcou hodnotou


def comparison_errors():
    x = None
    y = 0

    # Opravené porovnanie - '=' nahradené '=='
    if y == 1:
        print("y je 1")

    # Opravené porovnanie s None pomocou 'is'
    if x is None:
        print("x je None")

    # Opravené porovnanie float hodnôt s toleranciou chyby
    f1 = 0.1 + 0.2
    if abs(f1 - 0.3) < 1e-9:
        print("f1 je približne 0.3")

    # Opravené použitie 'is' na čísla (použitie '==' na hodnotové porovnanie)
    z = 1000
    if z == 1000:
        print("z je 1000")

    # Opravené porovnanie bez premennej
    if y == 0:
        print("y je 0")


def main():
    # Testovanie opraveného použitia znaku rovnosti
    equality_issues()
    comparison_errors()


if __name__ == "__main__":
    main()
