num = int(input())

if (num >= 1) and (num <= 9):
    print(("   _~_" + '    ') * num,
          ("  (o o)" + '   ') * num,
          (" /  V  \\" + '  ') * num,
          ("/(  _  )\\" + ' ') * num,
          ("  ^^ ^^  " + ' ') * num, sep='\n')
