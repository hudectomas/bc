#Chyby špecifické pre Mypy
def mypy_test(number: int) -> str:
    # Chyba typu (Mypy odhalí nekompatibilitu)
    result = number + "text"
    return result

def main():
    value = mypy_test(10)
    print(value)

if __name__ == "__main__":
    main()
