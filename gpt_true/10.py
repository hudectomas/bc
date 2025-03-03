# Nepoužité alebo chýbajúce importy - dlhší program s viacerými chybami

# Chyba 1: Nepoužitý import
import random  
import os  

def generate_random_number():
    # Chyba 2: Chýbajúci import pre 'math'
    return math.sqrt(25)

def read_file():
    # Chyba 3: Použitie modulu bez importu
    with open("example.txt", "r") as file:
        content = file.read()
    return content

def use_datetime():
    # Chyba 4: Použitie neimportovaného modulu
    now = datetime.datetime.now()
    print("Aktuálny dátum a čas:", now)

def unused_function():
    # Chyba 5: Definícia nevolanej funkcie
    def helper_function():
        return "Táto funkcia nie je nikdy použitá"

def main():
    try:
        # Testovanie chýbajúceho importu
        print("Náhodné číslo:", generate_random_number())
    except NameError:
        print("Chyba: Chýbajúci import modulu 'math'")

    try:
        # Testovanie čítania súboru bez chyby importu
        content = read_file()
        print("Obsah súboru:", content)
    except FileNotFoundError:
        print("Chyba: Súbor 'example.txt' neexistuje")
    except NameError:
        print("Chyba: Chýbajúci import pri práci so súbormi")

    try:
        # Testovanie neimportovaného modulu datetime
        use_datetime()
    except NameError:
        print("Chyba: Chýbajúci import modulu 'datetime'")

    # Nepoužitý import a funkcia
    unused_function()

if __name__ == "__main__":
    main()
