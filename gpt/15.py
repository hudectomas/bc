# Program so špecifickými chybami pre Mypy

def mypy_errors():
    try:
        # Chyba 1: Nesprávny typ návratu
        def wrong_return_type() -> int:
            return "toto nie je číslo"
        
        # Chyba 2: Nesprávne typovanie argumentu
        def add_numbers(a: int, b: int) -> int:
            return a + b
        
        print(add_numbers("10", 20))
        
    except Exception as e:
        print("Neočakávaná chyba:", e)

if __name__ == "__main__":
    mypy_errors()
