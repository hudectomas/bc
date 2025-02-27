def variable_overflow():
    # Pretečenie premenných
    try:
        big_number = 1
        for i in range(10000):
            big_number *= 2
        
        # Umelé obmedzenie veľkosti čísla (napodobnenie pretečenia)
        if big_number > 1e300:
            raise OverflowError("Pretečenie: hodnota je príliš veľká.")
        
        print("Konečná hodnota:", big_number)
    
    except OverflowError as e:
        print("Chyba pretečenia premenných:", e)


def main():
    # Testovanie pretečenia premenných
    variable_overflow()


if __name__ == "__main__":
    main()
