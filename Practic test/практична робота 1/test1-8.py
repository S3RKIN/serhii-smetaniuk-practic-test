
m = 8
total_combinations = 1

for i in range(m):
    total_combinations *= (25 - i)

print("Кількість можливих комбінацій:", total_combinations)
