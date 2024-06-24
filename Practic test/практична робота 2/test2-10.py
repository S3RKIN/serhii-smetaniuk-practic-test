def main():
    total_sum = 0
    count = 0
    print("Послідовність доатних чисел при введенні - зупинеться")
    while True:
        number = float(input("Введіть число: "))
        if number > 0:
            total_sum += number
            count += 1
        else:
            break
    
    if count > 0:
        average = total_sum / count
        print(f"Сума чисел: {total_sum}")
        print(f"Середнє арифметичне: {average}")
    else:
        print("Не було введено жодного додатнього числа.")

if __name__ == "__main__":
    main()
