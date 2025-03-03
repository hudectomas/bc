# Nedefinované premenné a funkcie - opravená verzia

import math  # Import potrebný pre výpočty

def calculate_area(radius):
    # Použitie správne definovanej premennej pi
    return math.pi * radius ** 2

def display_message(message):
    # Definovaná funkcia, aby ju bolo možné zavolať
    print(message)

def print_message():
    # Volanie existujúcej funkcie
    display_message("Toto je testovacia správa")

def undefined_in_loop():
    # Inicializácia premennej pred použitím v cykle
    undefined_variable = 2
    for i in range(5):
        result = undefined_variable * i
        print(result)

def conditional_error():
    # Definovanie oboch premenných pred použitím
    x = 10
    y = 20
    print(x, y)

def non_existent_function():
    # Definovaná funkcia, aby sa predišlo chybe pri volaní
    return "Táto funkcia teraz existuje!"

def call_defined_function():
    # Zavolanie teraz existujúcej funkcie
    return non_existent_function()

def main():
    try:
        # Testovanie výpočtu plochy kruhu
        print("Plocha kruhu:", calculate_area(5))
    except NameError:
        print("Chyba: Použitie nedefinovanej premennej")

    try:
        # Testovanie správne definovanej funkcie
        print_message()
    except NameError:
        print("Chyba: Volanie nedefinovanej funkcie")

    try:
        # Testovanie cyklu so správne inicializovanou premennou
        undefined_in_loop()
    except NameError:
        print("Chyba: Použitie nedefinovanej premennej v cykle")

    try:
        # Testovanie vetvenia s inicializovanými premennými
        conditional_error()
    except NameError:
        print("Chyba: Použitie nedefinovanej premennej vo vetvení")

    try:
        # Testovanie volania existujúcej funkcie
        print(call_defined_function())
    except NameError:
        print("Chyba: Pokus o zavolanie neexistujúcej funkcie")

if __name__ == "__main__":
    main()
