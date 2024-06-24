n = 5

if n < 0:
    result = 0
elif n == 0:
    result = 0
else:
    nn = int(str(n) * 2)
    nnn = int(str(n) * 3)
    result = n + nn + nnn

expected_result = 615

print( result)
print( expected_result)
