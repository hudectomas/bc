# Prístup mimo rozsah poľa - opravená verzia

def access_elements():
    my_list = [1, 2, 3, 4, 5]

    # Bezpečný prístup k indexu so zabezpečením rozsahu
    index = 4
    if index < len(my_list):
        print(my_list[index])
    else:
        print(f"Chyba: Index {index} je mimo rozsah.")

    # Bezpečný prístup k negatívnemu indexu
    index = -1
    if -len(my_list) <= index < len(my_list):
        print(my_list[index])
    else:
        print(f"Chyba: Negatívny index {index} je mimo rozsah.")

    # Správna kontrola dĺžky pred prístupom
    index = 5
    if index < len(my_list):
        print(my_list[index])
    else:
        print(f"Chyba: Index {index} je mimo rozsah.")

    # Cyklus so správnym rozsahom
    for i in range(len(my_list)):
        print(my_list[i])

    # Bezpečná manipulácia s indexom
    index = 2
    if index < len(my_list):
        print(my_list[index])
    else:
        print(f"Chyba: Index {index} je mimo rozsah.")


def string_access():
    text = "Python"

    # Bezpečný prístup k znakom reťazca
    index = 5
    if index < len(text):
        print(text[index])
    else:
        print(f"Chyba: Index {index} je mimo rozsah.")

    # Bezpečný rez reťazca
    start, end = 2, 10
    end = min(end, len(text))  # Orezanie na maximálnu dĺžku
    print(text[start:end])

    # Bezpečný prístup cez negatívny index
    index = -2
    if -len(text) <= index < len(text):
        print(text[index])
    else:
        print(f"Chyba: Negatívny index {index} je mimo rozsah.")

    # Správna manipulácia so zoznamom
    elements = ["a", "b", "c"]
    if len(elements) > 2:
        del elements[2]
    if len(elements) > 2:
        print(elements[2])
    else:
        print("Chyba: Prístup k neexistujúcemu prvku v liste.")


def main():
    # Testovanie opravených funkcií
    access_elements()
    string_access()


if __name__ == "__main__":
    main()
