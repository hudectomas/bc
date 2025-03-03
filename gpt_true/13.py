# Program opravený pre Pyflakes

def pyflakes_errors():
    try:
        # Odstránený nepoužitý import (sys bol nepoužitý, takže ho netreba)
        
        # Definovaná premenná pred použitím
        neexistujuca_premenna = "Toto je definovaná premenná"
        print(neexistujuca_premenna)
        
        # Zmenené typy premenných, aby nedošlo k nejednoznačnej redefinícii
        a = 10
        b = "text"
        print("Celé číslo:", a)
        print("Reťazec:", b)

    except Exception as e:
        print("Neočakávaná chyba:", e)

if __name__ == "__main__":
    pyflakes_errors()
