def vypocitaj_priemer(zoznam):
    return sum(zoznam) / len(zoznam)

def dlha_funkcia_s_dlhym_nazvom_pre_testovanie_pylintu(a, b, c, d, e, f, g, h, i, j):
    return a + b + c + d + e + f + g + h + i + j

# Chyba: Dlhá funkcia (Pylint: R0915)
vysledok1 = dlha_funkcia_s_dlhym_nazvom_pre_testovanie_pylintu(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Chyba: Príliš veľa lokálnych premenných (Pylint: R0914)
def funkcia_s_mnohymi_premennymi():
    var1 = 1
    var2 = 2
    var3 = 3
    var4 = 4
    var5 = 5
    var6 = 6
    var7 = 7
    var8 = 8
    var9 = 9
    var10 = 10
    var11 = 11
    var12 = 12
    var13 = 13
    var14 = 14
    var15 = 15
    return var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15

vysledok2 = funkcia_s_mnohymi_premennymi()

print(vysledok1, vysledok2)

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
priemer = vypocitaj_priemer(dlhy_zoznam)
print(priemer)

# Zbytočný kód
u = 10
v = 20
w = 30
x = 40
y = 50
z = 60
aa = 70
bb = 80
cc = 90
dd = 100