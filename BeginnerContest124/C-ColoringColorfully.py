# -*- coding: utf-8 -*-

# 文字列の入力
s = str(input())

# 配列に一文字ずつ格納
colors = list(s)

prev = int(colors[0])
changeCnt = 0

for i in range(1,len(colors)):

    if prev == int(colors[i]):
        colors[i] = abs(int(colors[i])-1)
        changeCnt += 1
    
    prev = int(colors[i])

# 出力
print(str(changeCnt))
