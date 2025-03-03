# Program opravený pre Flake8

def flake8_errors():
    try:
        # Opravené zbytočné medzery
        a = 10

        # Pridaný prázdny riadok pred definíciou funkcie
        def func():
            print("Správne naformátovaná funkcia")

        # Rozdelenie dlhého riadku na viacero častí
        print(
            "Tento riadok bol rozdelený, "
            "aby neprekročil maximálnu odporúčanú dĺžku znakov, "
            "čo spôsobovalo problém vo Flake8."
        )

        func()

    except Exception as e:
        print("Neočakávaná chyba:", e)


if __name__ == "__main__":
    flake8_errors()
