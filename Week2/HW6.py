num1 = int(input())
num2 = int(input())

if num2 % (num2 - num1 + 1) == 0:
    print('YES')
else:
    print('NO')
