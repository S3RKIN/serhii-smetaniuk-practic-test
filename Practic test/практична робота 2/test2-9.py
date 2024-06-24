#a, b = 0, 1
#while b < 100: 
    #print(b, end=' ')
    #a, b = b, a + b

a, b = 0, 1
index = 1
start_index = 5
end_index = 20
fib_sequence = []

while index <= end_index:
    if index >= start_index:
        fib_sequence.append(b)
    a, b = b, a + b
    index += 1

print(fib_sequence)
