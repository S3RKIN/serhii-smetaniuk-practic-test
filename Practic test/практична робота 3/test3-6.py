def main():
    a = int(input("Введіть число a: "))
    b = int(input("Введіть число b: "))
    if a != b:
        max_value = max(a, b)
        a = max_value
        b = max_value
    else:
        a = 0
        b = 0

    print(f"Змінене значення a: {a}")
    print(f"Змінене значення b: {b}")

if __name__ == "__main__":
    main()
