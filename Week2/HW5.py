x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if ((x1 - x2 <= 1) and (x1 - x2 >= -1)) and \
        ((y1 - y2 <= 1) and (y1 - y2 >= -1)):
    print('Yes')
else:
    print('No')