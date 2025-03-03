# Nesprávny počet argumentov - opravená verzia

def greet(name, age):
    # Funkcia na vypísanie pozdravu s menom a vekom
    print(f"Ahoj {name}, máš {age} rokov!")

def add(a, b):
    # Funkcia na sčítanie dvoch čísel
    return a + b

def multiply(a, b, c):
    # Funkcia na vynásobenie troch čísel
    return a * b * c

def show_message(message):
    # Funkcia na zobrazenie správy
    print(message)

def process_list(data, operation):
    # Bezpečné spracovanie zoznamu s volaním operácie na každej položke
    if callable(operation):
        for item in data:
            operation(item)
    else:
        print("Chyba: operation nie je volateľná funkcia")

def subtract(a, b, c):
    # Funkcia na odčítanie troch čísel
    return a - b - c

def calculate(a, b, c, d):
    # Funkcia na výpočet vzorca (a + b) * (c - d)
    return (a + b) * (c - d)

def main():
    # Hlavná funkcia, ktorá volá všetky ostatné funkcie so správnymi argumentmi
    greet("Jozef", 30)  
    greet("Anna", 25)  
    
    result = add(10, 5)  
    print("Súčet:", result)

    product = multiply(2, 3, 4)  
    print("Násobenie:", product)

    process_list([1, 2, 3], print)  

    result_subtract = subtract(5, 2, 1)  
    print("Odčítanie:", result_subtract)

    result_add = add(10, 20)  
    print("Súčet:", result_add)

    total = calculate(10, 5, 8, 3)  
    print("Výsledok výpočtu:", total)

    greet("Peter", 40)  

    show_message("Správa")  

if __name__ == "__main__":
    main()
