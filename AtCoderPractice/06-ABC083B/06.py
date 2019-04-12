# -*- coding: utf-8 -*-

total = 0

# 整数の入力
n,a,b = map(int, input().split())

for i in range(1,n+1):
    tmpKazu = str(i)
    tmpWa = 0
    for j in range(len(tmpKazu)):
        tmpWa += int(tmpKazu[j])

    if tmpWa >= a and tmpWa <= b :
        total += i

print(total)