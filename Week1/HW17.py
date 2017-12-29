num = int(input())

print(str(num // 3600 % 24) + ':', end='')
print(str(num % 3600 // 60 // 10) + str(num % 3600 // 60 % 10) + ":", end='')
print(str(num % 60 // 10) + str(num % 60 % 10))
