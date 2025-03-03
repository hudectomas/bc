# Rekurzia - dlhší program s viacerými chybami

def infinite_recursion(n):
    # Chyba 1: Nekonečná rekurzia bez podmienky zastavenia
    return infinite_recursion(n + 1)

def faulty_factorial(n):
    # Chyba 2: Nesprávne implementovaný faktoriál
    if n == 0:
        return 1
    else:
        return n * faulty_factorial(n)  # Chýba korektná podmienka zastavenia

def indirect_recursion_a(x):
    # Chyba 3: Nepriamy cyklus medzi dvoma funkciami
    return indirect_recursion_b(x)

def indirect_recursion_b(x):
    return indirect_recursion_a(x)

def nested_recursion(n):
    # Chyba 4: Zbytočne zložitá rekurzia bez kontroly hĺbky
    if n > 0:
        return nested_recursion(nested_recursion(n - 1))
    return 0

def main():
    try:
        # Testovanie nekonečnej rekurzie
        infinite_recursion(1)
    except RecursionError:
        print("Chyba: Pretečenie zásobníka pri nekonečnej rekurzii")

    try:
        # Testovanie chybného faktoriálu
        print(faulty_factorial(5))
    except RecursionError:
        print("Chyba: Pretečenie zásobníka pri výpočte faktoriálu")

    try:
        # Testovanie nepriamej rekurzie
        indirect_recursion_a(1)
    except RecursionError:
        print("Chyba: Pretečenie zásobníka pri nepriamej rekurzii")

    try:
        # Testovanie zložitej vnorenej rekurzie
        nested_recursion(10)
    except RecursionError:
        print("Chyba: Pretečenie zásobníka pri vnorenej rekurzii")

if __name__ == "__main__":
    main()
