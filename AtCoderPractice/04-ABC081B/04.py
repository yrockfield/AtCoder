# -*- coding: utf-8 -*-

canContinue = True
cnt = -1
# 整数の入力
a = int(input())
# スペース区切りの整数の入力
kazu = list(map(int, input().split()))

while canContinue:
    cnt += 1

    for i in range(a):
        if kazu[i] % 2 == 0:
            kazu[i] = kazu[i] /2
        else:
            canContinue = False
            break 

print(cnt)
