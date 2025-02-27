def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

def add_numbers(a, b):
    return a + b

def is_valid_number(num):
    # Neefektívny logický výraz
    if num >= 0 or num < 0:
        return True
    return False

def main():
    # Nesprávny počet argumentov (chýba jeden argument)
    greet("Alice")

    # Príliš veľa argumentov
    greet("Bob", 25, "extra")

    # Volanie funkcie s nesprávnym počtom argumentov
    result = add_numbers(5)
    print(f"Sum: {result}")

    # Správne volanie funkcie
    valid_result = add_numbers(3, 7)
    print(f"Valid sum: {valid_result}")

    # Neefektívny logický výraz
    print("Is 5 a valid number?:", is_valid_number(5))

if __name__ == "__main__":
    main()
