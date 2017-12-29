num = int(input())

num1 = int(input())
num2 = int(input())

print((num // (num1 - num2) -
       (num1 - (num % (num1 - num2))) // (num1 - num2)) + 1)
