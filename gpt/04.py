# Nesprávne použitie znaku rovnosti - dlhší program s viacerými chybami

def equality_issues():
    a = 5
    b = 10

    # Chyba 1: Použitie '=' namiesto '=='
    if a = b:
        print("a sa rovná b")

    # Chyba 2: Zbytočná porovnávacia podmienka
    if a == True:
        print("a je pravda")

    # Chyba 3: Porovnanie rôznych typov
    if a == "5":
        print("a je reťazec '5'")

    # Chyba 4: Nejednoznačné porovnanie
    if a is b:
        print("a a b sú rovnaké objekty")

    # Chyba 5: Chýbajúca hodnota na porovnanie
    if a == :
        print("Nekompletná podmienka")


def comparison_errors():
    x = None
    y = 0

    # Chyba 6: Použitie '=' v podmienke
    if y = 1:
        print("y je 1")

    # Chyba 7: Porovnanie s None nesprávnym spôsobom
    if x == None:
        print("x je None")

    # Chyba 8: Nesprávne porovnanie float hodnôt
    f1 = 0.1 + 0.2
    if f1 == 0.3:
        print("f1 je presne 0.3")

    # Chyba 9: Použitie 'is' na čísla
    z = 1000
    if z is 1000:
        print("z je 1000")

    # Chyba 10: Porovnanie bez premennej
    if == y:
        print("Neplatné porovnanie")


def main():
    # Testovanie nesprávneho použitia znaku rovnosti
    equality_issues()
    comparison_errors()


if __name__ == "__main__":
    main()
