# Manipulácia so súbormi - dlhší program s viacerými chybami

def file_operations():
    # Chyba 1: Otvorenie neexistujúceho súboru na čítanie
    try:
        file = open("nonexistent.txt", "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("Chyba: Súbor nebol nájdený.")
    finally:
        file.close()

    # Chyba 2: Zápis do súboru otvoreného len na čítanie
    try:
        file = open("example.txt", "r")
        file.write("Tento zápis zlyhá.")
    except IOError:
        print("Chyba: Nie je možné zapisovať do súboru.")
    finally:
        file.close()

    # Chyba 3: Zatvorenie súboru, ktorý už bol zatvorený
    file = open("example.txt", "w")
    file.close()
    file.close()

    # Chyba 4: Použitie súboru po jeho zatvorení
    try:
        file.write("Pokus o zápis po zatvorení súboru.")
    except ValueError:
        print("Chyba: Pokus o prácu so zatvoreným súborom.")

    # Chyba 5: Nesprávna manipulácia s CSV
    import csv
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[10])  # Prístup k neexistujúcemu stĺpcu
    except IndexError:
        print("Chyba: Prístup mimo rozsah stĺpcov CSV súboru.")


def main():
    # Testovanie chýb pri manipulácii so súbormi
    file_operations()


if __name__ == "__main__":
    main()
