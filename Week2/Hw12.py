'''
Даны три целых числа A, B, C.
Определить, есть ли среди них хотя бы одно четное и хотя бы одно нечетное.
'''
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 % 2 == 0 or num2 % 2 == 0 or num3 % 2 == 0:
    if num1 % 2 != 0 or num2 % 2 != 0 or num3 % 2 != 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')
