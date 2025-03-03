# Chyby špecifické pre Pyflakes
def pyflakes_test():
    unused_var = 42  # Pyflakes upozorní na nepoužitú premennú

    # Chýbajúca funkcia
    print_message("Toto je správa")  # Pyflakes nájde nedefinovanú funkciu

if __name__ == "__main__":
    pyflakes_test()
