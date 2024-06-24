#num = 0
#while num <= 20:
    #if num % 2 == 0:
     #   print(num, end=' ')
    #num += 1
    
    # Цикл для виводу кожного третього числа від -1 до -21
num = -1
count = 1
while num >= -21:
    if count % 3 == 0:
        print(num, end=' ')
    num -= 1
    count += 1
