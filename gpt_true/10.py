# Nepoužité alebo chýbajúce importy - opravená verzia

import math  
import datetime  

def generate_random_number():
    # Použitie modulu math
    return math.sqrt(25)

def read_file():
    # Použitie súboru s kontrolou existencie
    file_path = "example.txt"
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Chyba: Súbor 'example.txt' neexistuje."

def use_datetime():
    # Použitie modulu datetime
    now = datetime.datetime.now()
    print("Aktuálny dátum a čas:", now)

def helper_function():
    # Funkcia, ktorá sa teraz používa
    return "Táto funkcia je teraz použitá."

def main():
    try:
        # Testovanie správneho importu math
        print("Náhodné číslo:", generate_random_number())
    except NameError:
        print("Chyba: Chýbajúci import modulu 'math'")

    try:
        # Testovanie čítania súboru s kontrolou existencie
        content = read_file()
        print("Obsah súboru:", content)
    except NameError:
        print("Chyba: Chýbajúci import pri práci so súbormi")

    try:
        # Testovanie správneho importu datetime
        use_datetime()
    except NameError:
        print("Chyba: Chýbajúci import modulu 'datetime'")

    # Použitie pôvodne nepoužitej funkcie
    print(helper_function())

if __name__ == "__main__":
    main()
