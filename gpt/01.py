def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")


def main():
    # Nesprávny počet argumentov (chýba jeden argument)
    greet("Alice")

    # Príliš veľa argumentov
    greet("Bob", 25, "extra")


if __name__ == "__main__":
    main()
