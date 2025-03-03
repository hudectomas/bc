#Chyby špecifické pre Flake8
def flake8_test():
    # Dlhý riadok (Flake8 E501)
    message = "Toto je extrémne dlhý riadok, ktorý presahuje odporúčaný limit 79 znakov podľa PEP 8, čo spôsobí chybu vo Flake8."

    # Nejednotné odsadenie (Flake8 E101)
      x = 5
    y = 10

    return x + y

if __name__ == "__main__":
    flake8_test()
