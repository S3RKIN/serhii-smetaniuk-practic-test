def main():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))
    negative_count = 0
    if a < 0:
        negative_count += 1
    if b < 0:
        negative_count += 1
    if c < 0:
        negative_count += 1

    print(f"Кількість негативних чисел: {negative_count}")

if __name__ == "__main__":
    main()
