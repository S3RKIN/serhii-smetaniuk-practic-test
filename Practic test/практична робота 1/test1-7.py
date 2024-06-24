n = 10  
m = 3   

start = -n
if start % 2 != 0:  
    start += 1

for i in range(start, n + 1, m):
    if i % 2 == 0:
        print(i)
