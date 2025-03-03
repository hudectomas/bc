# Rekurzia - opravená verzia

def finite_recursion(n, limit=1000):
    # Rekurzia s podmienkou zastavenia
    if n >= limit:
        return n
    return finite_recursion(n + 1, limit)

def correct_factorial(n):
    # Správne implementovaný faktoriál s podmienkou zastavenia
    if n == 0 or n == 1:
        return 1
    return n * correct_factorial(n - 1)

def indirect_recursion_a(x, limit=10):
    # Bezpečná nepriamá rekurzia s kontrolou hĺbky
    if x > limit:
        return x
    return indirect_recursion_b(x + 1, limit)

def indirect_recursion_b(x, limit=10):
    return indirect_recursion_a(x + 1, limit)

def nested_recursion(n, depth=0, max_depth=10):
    # Bezpečná vnorena rekurzia s kontrolou hĺbky
    if n <= 0 or depth >= max_depth:
        return 0
    return nested_recursion(n - 1, depth + 1, max_depth)

def main():
    try:
        # Testovanie bezpečnej rekurzie
        print("Konečná rekurzia:", finite_recursion(1, 10))
    except RecursionError:
        print("Chyba: Pretečenie zásobníka")

    try:
        # Testovanie správneho faktoriálu
        print("Faktoriál 5:", correct_factorial(5))
    except RecursionError:
        print("Chyba: Pretečenie zásobníka pri výpočte faktoriálu")

    try:
        # Testovanie bezpečnej nepriamej rekurzie
        print("Nepriama rekurzia:", indirect_recursion_a(1))
    except RecursionError:
        print("Chyba: Pretečenie zásobníka pri nepriamej rekurzii")

    try:
        # Testovanie bezpečnej vnorenej rekurzie
        print("Vnorená rekurzia:", nested_recursion(10))
    except RecursionError:
        print("Chyba: Pretečenie zásobníka pri vnorenej rekurzii")

if __name__ == "__main__":
    main()
