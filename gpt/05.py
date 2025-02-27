def file_operations():
    # Manipulácia so súbormi
    try:
        file = open("example.txt", "r")
        content = file.read()
        print("Obsah súboru:", content)
        
        # Pokus o zápis do súboru otvoreného len na čítanie
        file.write("Pokus o zápis do súboru iba na čítanie.")
    
    except IOError as e:
        print("Chyba pri operácii so súborom:", e)
    
    finally:
        file.close()


def csv_operations():
    # Pokus o načítanie neexistujúceho CSV súboru
    try:
        with open("data.csv", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("Chyba: Súbor 'data.csv' neexistuje.")
    except Exception as e:
        print("Neočakávaná chyba pri práci s CSV súborom:", e)


def main():
    file_operations()
    
    # Testovanie manipulácie s neexistujúcim súborom
    csv_operations()


if __name__ == "__main__":
    main()
