# Prístup mimo rozsah poľa - dlhší program s viacerými chybami

def access_elements():
    my_list = [1, 2, 3, 4, 5]

    # Chyba 1: Index mimo rozsah
    print(my_list[10])

    # Chyba 2: Negatívny index mimo rozsah
    print(my_list[-6])

    # Chyba 3: Nesprávna kontrola dĺžky
    if len(my_list) >= 5:
        print(my_list[5])

    # Chyba 4: Cyklus cez neexistujúce indexy
    for i in range(10):
        print(my_list[i])

    # Chyba 5: Neplatný prístup k prvku
    index = 100
    print(my_list[index])


def string_access():
    text = "Python"

    # Chyba 6: Index mimo rozsah reťazca
    print(text[10])

    # Chyba 7: Rez s neplatným rozsahom
    print(text[2:10])

    # Chyba 8: Prístup cez negatívny index mimo rozsah
    print(text[-100])

    # Chyba 9: Nesprávna manipulácia so zoznamom
    elements = ["a", "b", "c"]
    elements[5] = "x"

    # Chyba 10: Prístup k neexistujúcemu prvku v liste
    del elements[2]
    print(elements[2])


def main():
    # Testovanie prístupu mimo rozsah poľa
    access_elements()
    string_access()


if __name__ == "__main__":
    main()
