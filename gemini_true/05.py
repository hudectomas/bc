def precitaj_subor(nazov_suboru):
    try:
        with open(nazov_suboru, "r") as subor:
            return subor.read()
    except FileNotFoundError:
        return None

def zapis_do_suboru(nazov_suboru, text):
    with open(nazov_suboru, "w") as subor:
        subor.write(text)

obsah1 = precitaj_subor("subor1.txt")
zapis_do_suboru("subor2.txt", "Ahoj svet!")

print(obsah1)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for cislo in dlhy_zoznam:
    zapis_do_suboru(f"subor_{cislo}.txt", str(cislo))