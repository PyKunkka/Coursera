'''
Заданы две клетки шахматной доски.
Если они покрашены в один цвет, то выведите слово YES,
а если в разные цвета – то NO.
'''

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

num1 = x1 + y1
num2 = x2 + y2

if num1 % 2 == 0:
    b = (num2 % 2 == 0)
else:
    b = (num2 % 2 != 0)

if b:
    print("Yes")
else:
    print("No")
