# Manipulácia so súbormi - opravená verzia

import csv

def file_operations():
    # Bezpečné otvorenie súboru s kontrolou existencie
    try:
        with open("nonexistent.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Chyba: Súbor nebol nájdený.")

    # Bezpečný zápis do súboru s overením režimu
    try:
        with open("example.txt", "w") as file:  # Zmena režimu na "w"
            file.write("Tento zápis je povolený.")
    except IOError:
        print("Chyba: Nie je možné zapisovať do súboru.")

    # Správne zatváranie súborov pomocou "with open"
    try:
        with open("example.txt", "w") as file:
            pass  # Súbor sa zatvorí automaticky
    except IOError as e:
        print(f"Chyba pri práci so súborom: {e}")

    # Overenie, či je súbor otvorený pred zápisom
    try:
        with open("example.txt", "w") as file:
            file.write("Pokus o zápis do otvoreného súboru.")
    except ValueError:
        print("Chyba: Pokus o prácu so zatvoreným súborom.")

    # Bezpečná manipulácia s CSV súborom
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 10:  # Overenie existencie stĺpca
                    print(row[10])
                else:
                    print("Chyba: Stĺpec neexistuje.")
    except FileNotFoundError:
        print("Chyba: CSV súbor neexistuje.")
    except IndexError:
        print("Chyba: Prístup mimo rozsah stĺpcov CSV súboru.")


def main():
    # Testovanie opravených funkcií pre manipuláciu so súbormi
    file_operations()


if __name__ == "__main__":
    main()
