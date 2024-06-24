import math

def main():
    x1 = float(input("Введіть координату x1 для точки А: "))
    y1 = float(input("Введіть координату y1 для точки А: "))
    x2 = float(input("Введіть координату x2 для точки В: "))
    y2 = float(input("Введіть координату y2 для точки В: "))
    distance_A = math.sqrt(x1**2 + y1**2) 
    distance_B = math.sqrt(x2**2 + y2**2)
    if distance_A < distance_B:
        print("Точка А ближче до початку координат.")
    elif distance_B < distance_A:
        print("Точка В ближче до початку координат.")
    else:
        print("Обидві точки знаходяться на однаковій відстані від початку координат.")

if __name__ == "__main__":
    main()
