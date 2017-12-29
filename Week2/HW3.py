'''
Даны три целых числа. Найдите наибольшее из них (программа должна вывести ровно одно целое число).

Какое наименьшее число операторов сравнения (>, <, >=, <=) необходимо для решения этой задачи?
'''
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num3 and num2 >= num1:
    print(num2)
else:
    print(num3)
