def main():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))
    k = float(input("Введіть число k: "))
    if k == 0:
        print("Дільник не може бути нулем.")
        return
    if a % k == 0:
        print(f"Число k = {k} є дільником числа a = {a}")
    else:
        print(f"Число k = {k} не є дільником числа a = {a}")
    if b % k == 0:
        print(f"Число k = {k} є дільником числа b = {b}")
    else:
        print(f"Число k = {k} не є дільником числа b = {b}")
    if c % k == 0:
        print(f"Число k = {k} є дільником числа c = {c}")
    else:
        print(f"Число k = {k} не є дільником числа c = {c}")

if __name__ == "__main__":
    main()
