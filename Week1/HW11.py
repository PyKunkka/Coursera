num1 = int(input())    # стоимость в рублях
num2 = int(input())    # копейки
num = int(input())     # кол. пирожков

num3 = (num2 * num) // 100

print(num1 * num + num3, (num2 * num) % 100)
