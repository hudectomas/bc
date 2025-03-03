# Delenie nulou - dlhší program s viacerými chybami

def division_errors():
    a = 10
    b = 0

    # Chyba 1: Priame delenie nulou
    try:
        result = a / b
    except ZeroDivisionError:
        print("Chyba: Pokus o delenie nulou (/)")

    # Chyba 2: Delenie nulou pomocou celočíselného delenia
    try:
        result = a // b
    except ZeroDivisionError:
        print("Chyba: Pokus o celočíselné delenie nulou (//)")

    # Chyba 3: Modulárna operácia s nulou
    try:
        result = a % b
    except ZeroDivisionError:
        print("Chyba: Pokus o zvyšok po delení nulou (%)")

    # Chyba 4: Delenie premennou, ktorá je nula
    try:
        x = 100
        y = 0
        result = x / y
    except ZeroDivisionError:
        print("Chyba: Delenie premennej s hodnotou 0")

    # Chyba 5: Delenie nulou v cykle
    for i in range(5):
        try:
            result = i / (i - 2)
        except ZeroDivisionError:
            print(f"Chyba: Delenie nulou v iterácii {i}")

    # Chyba 6: Delenie nulou v lambda funkcii
    try:
        divide = lambda x, y: x / y
        print(divide(10, 0))
    except ZeroDivisionError:
        print("Chyba: Delenie nulou v lambda funkcii")

    # Chyba 7: Nepodchytené delenie nulou
    result = a / b  # Táto línia spôsobí výnimku, ak nie je v bloku try


def main():
    # Testovanie chýb pri delení nulou
    division_errors()


if __name__ == "__main__":
    main()
