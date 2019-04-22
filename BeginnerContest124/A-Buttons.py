# -*- coding: utf-8 -*-

# スペース区切りの整数の入力
a, b = map(int, input().split())
coins = 0

for i in range(2):
    if a >= b :
        coins += a
        a -= 1
    else:
        coins += b
        b -= 1

# 出力
print(str(coins))
