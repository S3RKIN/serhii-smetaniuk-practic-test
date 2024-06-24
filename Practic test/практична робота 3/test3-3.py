def main():
    angle1 = float(input("Введіть величину першого кута (в градусах): "))
    angle2 = float(input("Введіть величину другого кута (в градусах): "))
    angle3 = 180 - angle1 - angle2
    if angle1 > 0 and angle2 > 0 and angle3 > 0:
        print("Такий трикутник існує.")
        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            print("Цей трикутник є прямокутним.")
        else:
            print("Цей трикутник не є прямокутним.")
    else:
        print("Трикутник з такими кутами не існує.")

if __name__ == "__main__":
    main()