# -*- coding: utf-8 -*-

totalAlice = 0
totalBob = 0

# 整数の入力
a = int(input())
# スペース区切りの整数の入力
cards = list(map(int, input().split()))

# ソート
cards.sort(reverse=True)

for i in range(len(cards)):
    if i % 2 == 0:
        totalAlice += cards[i]
    else:
        totalBob += cards[i]

print(totalAlice - totalBob)