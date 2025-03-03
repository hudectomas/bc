# Delenie nulou - opravená verzia

def safe_divide(a, b):
    # Bezpečné delenie s kontrolou delenia nulou
    if b == 0:
        print("Chyba: Pokus o delenie nulou!")
        return None
    return a / b

def safe_integer_divide(a, b):
    # Bezpečné celočíselné delenie
    if b == 0:
        print("Chyba: Pokus o celočíselné delenie nulou!")
        return None
    return a // b

def safe_modulo(a, b):
    # Bezpečná modulárna operácia
    if b == 0:
        print("Chyba: Pokus o modulo nulou!")
        return None
    return a % b

def division_errors():
    a = 10
    b = 0

    # Použitie bezpečných deliacich funkcií
    print("Bezpečné delenie:", safe_divide(a, b))
    print("Bezpečné celočíselné delenie:", safe_integer_divide(a, b))
    print("Bezpečné modulo:", safe_modulo(a, b))

    # Delenie premennou, ktorá je nula
    x = 100
    y = 0
    print("Delenie premennej:", safe_divide(x, y))

    # Bezpečné delenie v cykle
    for i in range(5):
        denominator = i - 2
        print(f"Delenie v iterácii {i}:", safe_divide(i, denominator))

    # Bezpečné delenie v lambda funkcii
    safe_lambda_divide = lambda x, y: safe_divide(x, y)
    print("Bezpečné lambda delenie:", safe_lambda_divide(10, 0))


def main():
    # Testovanie opravených funkcií pri delení nulou
    division_errors()


if __name__ == "__main__":
    main()
