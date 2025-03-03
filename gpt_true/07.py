# Pretečenie premenných - opravená verzia

def variable_overflow():
    # Bezpečné násobenie s limitom
    big_number = 1
    for i in range(10):  # Znížený rozsah, aby sa predišlo pretečeniu
        big_number *= 10 ** 5

    print("Veľké číslo po cykle:", big_number)

    # Bezpečná manipulácia s veľkým reťazcom
    large_string = "A"
    try:
        for _ in range(20):  # Pridaný pevný limit
            large_string += large_string
    except MemoryError:
        print("Chyba: Pretečenie pamäte pri reťazci")

    # Bezpečný prístup k zoznamu s overením indexu
    big_list = [0] * 100
    index = 10**6
    if index < len(big_list):
        value = big_list[index]
    else:
        print(f"Chyba: Index {index} je mimo rozsah zoznamu.")

    # Ošetrený nekonečný cyklus s maximálnym limitom
    counter = 0
    max_limit = 1_000_000  # Nastavenie bezpečného limitu
    while counter < max_limit:
        counter += 1

    print("Počítadlo dosiahlo limit:", counter)

    # Bezpečná rekurzia s podmienkou zastavenia
    def recursive_safe(n, limit=1000):
        if n > limit:
            return n
        return recursive_safe(n + 1, limit)

    try:
        result = recursive_safe(1)
        print("Bezpečná rekurzia skončila pri hodnote:", result)
    except RecursionError:
        print("Chyba: Pretečenie zásobníka pri rekurzii")


def main():
    # Testovanie opravených funkcií pre pretečenie premenných
    variable_overflow()


if __name__ == "__main__":
    main()
