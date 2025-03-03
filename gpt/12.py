def unused_function():
    pass  # Chyba: nevyužitá funkcia

def inconsistent_naming():
    MyVariable = 10  # Chyba: nekonzistentné pomenovanie (CamelCase namiesto snake_case)
    return MyVariable

def main():
    value = inconsistent_naming()
    print("Hodnota premennej:", value)

if __name__ == "__main__":
    main()
