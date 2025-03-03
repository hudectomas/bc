# Program opravený pre Pylint

def pylint_errors():
    try:
        # Použitie premennej, aby nebola nepoužitá
        used_variable = 42
        print("Použitá premenná:", used_variable)

        # Správne pomenovanie konštanty (konštanty sa v Pythone píšu veľkými písmenami)
        MY_CONSTANT = 100
        print("Konštanta:", MY_CONSTANT)

        # Funkcia teraz vracia hodnotu namiesto prázdneho tela
        def meaningful_function():
            return "Táto funkcia teraz niečo vracia"

        print(meaningful_function())

    except Exception as e:
        print("Neočakávaná chyba:", e)

if __name__ == "__main__":
    pylint_errors()
