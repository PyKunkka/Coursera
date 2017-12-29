num = int(input())

num1 = num // 100
num2 = num % 100

num2 = num2 % 10 * 10 + num2 // 10

print(num2 - num1 + 1)
