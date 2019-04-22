# -*- coding: utf-8 -*-
import copy
import math

# 整数の入力
n = int(input())

capa = []

capa=[int(input()) for i in range(5)]

# 各交通機関のうち、運べる人数が一番少ないものをベースとする
capa_min = min(capa)

ans = n//capa_min 

# if n <= capa_min:
#     amari = 0
# else:
amari = n % capa_min

# 人数が割り切れたら
if amari != 0:
    ans += 5
else:
    ans += 4
    
print (str(ans))



# 以下の処理だとタイムオーバーになるからNG
# toshi = [n,0,0,0,0,0]
# next_toshi = copy.deepcopy(toshi)
# time = 0

# while toshi[5] != n:
#     # print("toshi[0]:{},[1]:{},[2]:{},[3]:{},[4]:{},[5]:{}".format(toshi[0],toshi[1],toshi[2],toshi[3],toshi[4],toshi[5]))
#     time += 1
#     for i in range(len(toshi)-1):
#         if toshi[i] != 0:
#             if toshi[i] > capa[i]:
#                 next_toshi[i] = next_toshi[i] - capa[i]
#                 next_toshi[i+1] = toshi[i+1]  + capa[i]
#             else:
#                 next_toshi[i] = next_toshi[i] - toshi[i]
#                 next_toshi[i+1] = toshi[i+1] + toshi[i] 
#         # print("toshi[{}]:{},toshi[{}]:{}".format(i,next_toshi[i],i+1,next_toshi[i+1]))
#     toshi = copy.deepcopy(next_toshi)
#     # print("next_toshi[0]:{},[1]:{},[2]:{},[3]:{},[4]:{},[5]:{}".format(next_toshi[0],next_toshi[1],next_toshi[2],next_toshi[3],next_toshi[4],next_toshi[5]))
        
# print(str(time))
