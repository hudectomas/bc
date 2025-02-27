def check_equality(a, b):
    # Nesprávne použitie znaku rovnosti
    if a = b:
        print("Values are equal!")
    else:
        print("Values are not equal!")


def main():
    x = 5
    y = 10

    # Pokus o porovnanie
    check_equality(x, y)


if __name__ == "__main__":
    main()
