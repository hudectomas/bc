# Program so špecifickými chybami pre Pyflakes

def pyflakes_errors():
    try:
        # Chyba 1: Import, ktorý sa nepoužíva
        import sys
        
        # Chyba 2: Nedefinovaná premenná
        print(neexistujuca_premenna)
        
        # Chyba 3: Redefinícia premennej
        a = 10
        a = "text"
        
    except Exception as e:
        print("Neočakávaná chyba:", e)

if __name__ == "__main__":
    pyflakes_errors()
