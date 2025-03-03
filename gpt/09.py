# Nedefinované premenné a funkcie - dlhší program s viacerými chybami

def calculate_area(radius):
    # Chyba 1: Použitie nedefinovanej premennej
    return pi * radius ** 2

def print_message():
    # Chyba 2: Volanie nedefinovanej funkcie
    display_message("Toto je testovacia správa")

def undefined_in_loop():
    # Chyba 3: Použitie nedefinovanej premennej v cykle
    for i in range(5):
        result = undefined_variable * i
        print(result)

def conditional_error():
    # Chyba 4: Nedefinovaná premenná vo vetvení
    if True:
        x = 10
    print(x, y)  # 'y' nie je definované

def call_undefined_function():
    # Chyba 5: Pokus o zavolanie funkcie, ktorá neexistuje
    return non_existent_function()

def main():
    try:
        # Testovanie výpočtu s nedefinovanou premennou
        calculate_area(5)
    except NameError:
        print("Chyba: Použitie nedefinovanej premennej 'pi'")

    try:
        # Testovanie volania nedefinovanej funkcie
        print_message()
    except NameError:
        print("Chyba: Volanie nedefinovanej funkcie 'display_message'")

    try:
        # Testovanie cyklu s nedefinovanou premennou
        undefined_in_loop()
    except NameError:
        print("Chyba: Použitie nedefinovanej premennej 'undefined_variable'")

    try:
        # Testovanie vetvenia s nedefinovanou premennou
        conditional_error()
    except NameError:
        print("Chyba: Použitie nedefinovanej premennej 'y'")

    try:
        # Testovanie zavolania neexistujúcej funkcie
        call_undefined_function()
    except NameError:
        print("Chyba: Pokus o zavolanie neexistujúcej funkcie 'non_existent_function'")

if __name__ == "__main__":
    main()
