def main():
    numbers = []
    for i in range(3):
        number = float(input(f"Введіть число {i+1}: "))
        numbers.append(number)
    for i, num in enumerate(numbers):
        if num >= 0:
            numbers[i] = num ** 2  
        else:
            numbers[i] = num ** 4 

    for i, num in enumerate(numbers):
        print(f"Результат для числа {i+1}: {num}")

if __name__ == "__main__":
    main()
