# Nekonzistentnosť argumentov a premenných - opravená verzia

def greet(name, age):
    # Opravené: správne použitie argumentu age
    print("Ahoj,", name)
    print("Máš", age, "rokov")

def calculate_sum(a, b, c=0):
    # Opravené: pridaný predvolený argument pre prípad volania s dvoma argumentmi
    return a + b + c

def update_list(my_list):
    # Opravené: správny názov premennej a pridanie prvku do zoznamu
    my_list.append(10)
    return my_list

def display_info(first_name, last_name=""):
    # Opravené: správne predvolené hodnoty bez nekonzistencie
    print("Meno:", first_name, last_name)

def multiply_numbers(x, y, z=1):
    # Opravené: pridaný argument z, aby sa zabránilo chybe nedefinovanej premennej
    return x * y * z

def main():
    try:
        # Testovanie správneho volania funkcie greet
        greet("Ján", 25)
    except NameError:
        print("Chyba: Nesprávny názov premennej")

    try:
        # Testovanie správneho počtu argumentov
        result = calculate_sum(1, 2, 3)
        print("Súčet:", result)

        result = calculate_sum(1, 2)  # Volanie s dvoma argumentmi, c=0
        print("Súčet s predvoleným argumentom:", result)
    except TypeError:
        print("Chyba: Nesprávny počet argumentov pri volaní funkcie 'calculate_sum'")

    try:
        # Testovanie správneho spracovania zoznamu
        my_list = [1, 2, 3]
        updated_list = update_list(my_list)
        print("Aktualizovaný zoznam:", updated_list)
    except NameError:
        print("Chyba: Nesprávny názov premennej")

    try:
        # Testovanie správneho použitia predvolených argumentov
        display_info("Anna")
        display_info("Peter", "Novák")
    except Exception as e:
        print("Neočakávaná chyba pri zobrazení informácií:", e)

    try:
        # Testovanie správneho použitia argumentov vo výpočte
        result = multiply_numbers(3, 4)
        print("Výsledok násobenia:", result)

        result = multiply_numbers(3, 4, 2)  # Volanie s tromi argumentmi
        print("Výsledok násobenia s tromi argumentmi:", result)
    except NameError:
        print("Chyba: Použitie nedefinovanej premennej")

if __name__ == "__main__":
    main()
