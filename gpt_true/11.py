# Nekonzistentnosť argumentov a premenných - dlhší program s viacerými chybami

def greet(name, age):
    # Chyba 1: Nekonzistentné použitie argumentov
    print("Ahoj,", name)
    print("Máš", years, "rokov")  # Nesprávny názov premennej

def calculate_sum(a, b, c):
    # Chyba 2: Nesprávny počet argumentov pri volaní
    return a + b + c

def update_list(my_list):
    # Chyba 3: Zmätok v názvoch premenných
    myList.append(10)  # Nesprávny názov premennej
    return my_list

def display_info(first_name, last_name=""):
    # Chyba 4: Nekonzistentné použitie predvolených hodnôt
    print("Meno:", first_name, last_name)

def multiply_numbers(x, y):
    # Chyba 5: Použitie nesprávnej premennej vo výpočte
    return x * z  # 'z' nie je argument

def main():
    try:
        # Testovanie nekonzistentných názvov premenných
        greet("Ján", 25)
    except NameError:
        print("Chyba: Nekonzistentný názov premennej 'years'")

    try:
        # Testovanie nesprávneho počtu argumentov
        result = calculate_sum(1, 2)
        print("Súčet:", result)
    except TypeError:
        print("Chyba: Nesprávny počet argumentov pri volaní funkcie 'calculate_sum'")

    try:
        # Testovanie zmätku v názvoch premenných
        my_list = [1, 2, 3]
        updated_list = update_list(my_list)
        print("Aktualizovaný zoznam:", updated_list)
    except NameError:
        print("Chyba: Nesprávny názov premennej 'myList'")

    try:
        # Testovanie predvolených argumentov
        display_info("Anna")
        display_info("Peter", "Novák")
    except Exception as e:
        print("Neočakávaná chyba pri zobrazení informácií:", e)

    try:
        # Testovanie nesprávnej premennej vo výpočte
        result = multiply_numbers(3, 4)
        print("Výsledok násobenia:", result)
    except NameError:
        print("Chyba: Použitie nedefinovanej premennej 'z'")

if __name__ == "__main__":
    main()
