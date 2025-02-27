#chyby pre pyflakes
def funkcia():
    x = 10
    y = 20
    # Chyba: Nepoužitá lokálna premenná 'y'

    print(x)

def ina_funkcia():
    z = 30
    # Chyba: Použitie nedefinovanej premennej 'w'
    print(w)

funkcia()
ina_funkcia()

dlhy_zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for cislo in dlhy_zoznam:
    x = cislo
    # Chyba: Re-definícia lokálnej premennej 'x' v rámci loopu.
    print(x)

# Zbytočný kód
a = 10
b = 20
c = 30
d = 40
e = 50
f = 60
g = 70
h = 80
i = 90
j = 100