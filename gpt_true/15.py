# Program opravený pre Mypy

from typing import Union

def mypy_errors():
    try:
        # Opravený typ návratu, teraz vždy vracia celé číslo
        def correct_return_type() -> int:
            return 42

        # Opravené typovanie argumentov s kontrolou vstupných údajov
        def add_numbers(a: Union[int, str], b: int) -> int:
            if isinstance(a, str) and a.isdigit():
                a = int(a)
            elif not isinstance(a, int):
                raise ValueError("Argument 'a' musí byť celé číslo alebo číselný reťazec")
            
            return a + b

        print("Správny návratový typ:", correct_return_type())
        print("Súčet:", add_numbers(10, 20))
        print("Súčet so stringovým číslom:", add_numbers("10", 20))

    except Exception as e:
        print("Neočakávaná chyba:", e)


if __name__ == "__main__":
    mypy_errors()
