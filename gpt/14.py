# Program so špecifickými chybami pre Flake8

def flake8_errors():
    try:
        # Chyba 1: Zbytočné medzery
        a  =  10
        
        # Chyba 2: Chýbajúci prázdny riadok
        def func():print("Zle naformátovaná funkcia")
        
        # Chyba 3: Dlhý riadok
        print("Tento riadok je extrémne dlhý a prekračuje maximálnu odporúčanú dĺžku znakov, čo spôsobí problém vo Flake8.")
        
    except Exception as e:
        print("Neočakávaná chyba:", e)

if __name__ == "__main__":
    flake8_errors()
