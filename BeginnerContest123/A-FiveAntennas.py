# -*- coding: utf-8 -*-

# 整数の入力
antena = []

for i in range(5):
    antena.append(int(input()))

k = int(input())

for i in range(len(antena)):
    for j in range(i+1, len(antena)):
        dist = abs(antena[j] - antena[i])
        if dist > k:
            print(":(")
            exit()

# 出力
print("Yay!")
