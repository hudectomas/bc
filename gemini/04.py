a = 5
b = 10

# Chyba: Priradenie namiesto porovnania
if a = b:
    print("a a b sú rovnaké")

# Chyba: Priradenie namiesto porovnania
while a = 0:
    a -= 1

print(a, b)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for cislo in dlhy_zoznam:
    a = cislo

# Zbytočný kód
w = 40