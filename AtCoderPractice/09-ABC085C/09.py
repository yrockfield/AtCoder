# -*- coding: utf-8 -*-

# スペース区切りの整数の入力
n, y = map(int, input().split())
b10k = -1
ans=False

while b10k <= n:
        b10k += 1
        b5k = -1
        while b10k + b5k <= n:
                b5k += 1
                b1k = -1
                while b10k + b5k + b1k <= n:
                        b1k += 1

                        if b10k*10000 + b5k*5000 + b1k*1000 == y and b10k + b5k + b1k == n:
                                ans=True
                                break
                else:
                        continue
                break
        break

if ans==False:
        b10k = -1
        b5k = -1
        b1k = -1

print("{} {} {}".format(b10k,b5k,b1k))