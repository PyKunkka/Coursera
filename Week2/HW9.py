'''

'''
num = int(input())

if num % 10 == 1 and num != 11:
    print(num, 'korova')
elif 2 <= num % 10 <= 4 and num // 10 != 1:
    print(num, 'korovy')
else:
    print(num, 'korov')
