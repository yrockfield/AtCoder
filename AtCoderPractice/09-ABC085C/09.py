# -*- coding: utf-8 -*-

# スペース区切りの整数の入力
n, y = map(int, input().split())

for b10k in range(n+1):
        for b5k in range (n-b10k+1):
                if b10k*10000 + b5k*5000 + (n-b10k-b5k)*1000 == y:
                        print("{} {} {}".format(b10k,b5k,n-b10k-b5k))
                        exit()


print("-1 -1 -1")
