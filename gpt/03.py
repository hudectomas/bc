def access_list_element(lst, index):
    # Prístup mimo rozsah poľa
    return lst[index]


def main():
    numbers = [1, 2, 3]

    # Správny prístup k prvku
    print(f"Element at index 1: {access_list_element(numbers, 1)}")

    # Prístup mimo rozsah poľa
    out_of_range_element = access_list_element(numbers, 5)
    print(f"Element at index 5: {out_of_range_element}")


if __name__ == "__main__":
    main()