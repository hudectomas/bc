# Nepoužité importy
import math
import random

def calculate_square(number):
    # Chýbajúci import spôsobí chybu
    result = sqrt(number)  # Chyba: sqrt nie je definované (chýba `from math import sqrt`)
    return result

def main():
    number = 16
    square = calculate_square(number)
    print(f"Odmocnina čísla {number} je {square}")

if __name__ == "__main__":
    main()
