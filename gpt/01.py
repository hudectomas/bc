# Nesprávny počet argumentov - dlhší program s viacerými chybami

def greet(name, age):
    print(f"Ahoj {name}, máš {age} rokov!")

def add(a, b):
    return a + b

def multiply(a, b, c):
    return a * b * c

def show_message(message):
    print(message)

def process_list(data, operation):
    for item in data:
        operation(item)

def subtract(a, b, c):
    return a - b - c

def calculate(a, b, c, d):
    return (a + b) * (c - d)

def main():
    # Chyba 1: Príliš málo argumentov
    greet("Jozef")  
    
    # Chyba 2: Príliš veľa argumentov
    greet("Anna", 25, "extra_argument")

    # Chyba 3: Nedostatočný počet argumentov
    result = add(10)

    # Chyba 4: Zlý počet argumentov pri násobení
    product = multiply(2, 3)

    # Chyba 5: Prázdny callback
    process_list([1, 2, 3])

    # Chyba 6: Funkcia očakáva viac argumentov
    subtract(5, 2)

    # Chyba 7: Príliš veľa argumentov
    result = add(10, 20, 30)

    # Chyba 8: Chýbajúce argumenty vo funkcii so 4 parametrami
    total = calculate(10, 5)

    # Chyba 9: Funkcia volaná bez zátvoriek
    greet

    # Chyba 10: Funkcia očakáva menej argumentov
    show_message("Správa", "Extra argument")

if __name__ == "__main__":
    main()
