def infinite_recursion(n):
    # Nekonečná rekurzia
    if n == 0:
        return 1
    else:
        return infinite_recursion(n + 1)


def main():
    try:
        # Spustenie nekonečnej rekurzie
        infinite_recursion(1)
    except RecursionError:
        print("Chyba: Prekročený limit rekurzie.")


if __name__ == "__main__":
    main()
