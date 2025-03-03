def greet(name):
    print(f"Ahoj, {name}!")

def main():
    # Pokus o volanie nedefinovanej funkcie
    say_hello("Jozef")  # Chyba: funkcia say_hello neexistuje

    # Použitie nedefinovanej premennej
    print("Tvoja správa:", message)  # Chyba: message nebola definovaná

if __name__ == "__main__":
    main()
