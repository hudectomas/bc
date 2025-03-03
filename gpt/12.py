# Program so špecifickými chybami pre Pylint

def pylint_errors():
    try:
        # Chyba 1: Nepoužitá premenná
        nepouzita = 42
        
        # Chyba 2: Zlé pomenovanie premennej
        MY_CONSTANT = 100
        
        # Chyba 3: Funkcia bez návratovej hodnoty
        def empty_function():
            pass
        
        empty_function()
    except Exception as e:
        print("Neočakávaná chyba:", e)

if __name__ == "__main__":
    pylint_errors()
