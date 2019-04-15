# -*- coding: utf-8 -*-
import re

# 数値入力
n = int(input())

tprev = 0
xprev = 0
yprev = 0


for i in range(n):
        t,x,y = map(int,input().split())

        tmove = t - tprev
        xmove = abs(x - xprev)
        ymove = abs(y - yprev)

        if tmove - xmove - ymove < 0 : 
                print ("No")
                exit()
        elif (tmove - xmove - ymove) % 2 != 0:
                print("No")
                exit()

print("Yes")
