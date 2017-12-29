'''
Дано трехзначное число. Найдите сумму его цифр.
'''
num = int(input())

num1 = num % 10
num2 = num % 100

print(num1 + (num2 // 10) + (num // 100))
