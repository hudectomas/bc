zoznam = [1, 2, 3, 4, 5]

if len(zoznam) > 5:
    hodnota1 = zoznam[4]
else:
    hodnota1 = None

if len(zoznam) > 6:
    hodnota2 = zoznam[-1]
else:
    hodnota2 = None

print(hodnota1, hodnota2)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in range(len(dlhy_zoznam)):
    print(dlhy_zoznam[i])