num1 = int(input())
num2 = int(input())

print('YES' * (1 - (num1 % num2)) + 'NO' *
      ((((num1 % num2) + 2) // ((num1 % num2) + 1)) % 2))

print(7 % 3)