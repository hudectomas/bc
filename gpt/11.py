def add_numbers(a, b):
    return a + b

def main():
    x = 10
    y = "20"  # Chyba: nekonzistentný typ (int + str)

    # Pokus o sčítanie rôznych typov
    result = add_numbers(x, y)
    print("Výsledok sčítania:", result)

if __name__ == "__main__":
    main()
