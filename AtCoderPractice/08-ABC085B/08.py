# -*- coding: utf-8 -*-

# 整数の入力
n = int(input())
mochi = []

# 整数の入力:n行分の入力
for i in range(n):
    mochi.append(int(input()))

# ソート
mochi.sort()

for i in reversed (range(1,len(mochi))):
    if mochi[i] == mochi[i-1]:
        del mochi[i-1]
        i -= 1

print(len(mochi))