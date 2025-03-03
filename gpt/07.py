# Pretečenie premenných - dlhší program s viacerými chybami

def variable_overflow():
    # Chyba 1: Nekonečný rast čísla v cykle
    big_number = 1
    for i in range(100):
        big_number *= 10 ** 10

    print("Veľké číslo po cykle:", big_number)

    # Chyba 2: Pretečenie reťazca v slučke
    large_string = "A"
    try:
        while True:
            large_string += large_string
    except MemoryError:
        print("Chyba: Pretečenie pamäte pri reťazci")

    # Chyba 3: Prístup k extrémne veľkému indexu
    big_list = [0] * 100
    try:
        value = big_list[10**6]
    except IndexError:
        print("Chyba: Prístup mimo rozsah poľa")

    # Chyba 4: Pretečenie počítadla
    counter = 0
    try:
        while True:
            counter += 1
    except KeyboardInterrupt:
        print("Pretečenie počítadla, zastavené klávesnicou")

    # Chyba 5: Nekonečné volanie rekurzie (spôsobí pretečenie zásobníka)
    def recursive_overflow(n):
        return recursive_overflow(n + 1)

    try:
        recursive_overflow(1)
    except RecursionError:
        print("Chyba: Pretečenie zásobníka pri rekurzii")


def main():
    # Testovanie chýb súvisiacich s pretečením
    variable_overflow()


if __name__ == "__main__":
    main()
