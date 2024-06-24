def main():
    x = float(input("Введіть число x: "))
    y = float(input("Введіть число y: "))

    if x == y:
        print("Числа не повинні бути рівні одне одному.")
        return
    sum = (x + y) / 2
    double = 2 * x * y
    if x < y:
        x = sum
        y = double
    else:
        y = sum
        x = double
    print(f"Змінене значення x: {x}")
    print(f"Змінене значення y: {y}")
if __name__ == "__main__":
    main()
