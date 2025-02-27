zoznam = [1, 2, 3, 4, 5]

# Chyba: Index mimo rozsah
hodnota1 = zoznam[5]

# Chyba: Index mimo rozsah (záporný)
hodnota2 = zoznam[-6]

print(hodnota1, hodnota2)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in range(len(dlhy_zoznam) + 1):
    print(dlhy_zoznam[i])

# Zbytočný kód
z = 30