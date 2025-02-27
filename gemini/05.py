def precitaj_subor(nazov_suboru):
    subor = open(nazov_suboru, "r")
    obsah = subor.read()
    return obsah

# Chyba: Chýba zatvorenie súboru
obsah1 = precitaj_subor("subor1.txt")

def zapis_do_suboru(nazov_suboru, text):
    subor = open(nazov_suboru, "w")
    subor.write(text)

# Chyba: Chýba zatvorenie súboru
zapis_do_suboru("subor2.txt", "Ahoj svet!")

print(obsah1)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for cislo in dlhy_zoznam:
    zapis_do_suboru(f"subor_{cislo}.txt", str(cislo))

# Zbytočný kód
v = 50