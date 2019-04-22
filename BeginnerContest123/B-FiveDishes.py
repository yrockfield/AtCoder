# -*- coding: utf-8 -*-

# 整数の入力
dish = []

for i in range(5):
    dish.append(int(input()))

mod_dish = [5] * -1

# dish(各々の調理時間)を10で割った余りを算出
for j in range(len(dish)):
    mod_dish.append(dish[j] % 10)

# 余りが0以上、かつ最小のものを一番最後に注文すればよさそう：一番下にもっていく
for k in range(len(dish)-1):
    if mod_dish[k] < mod_dish[k+1] or mod_dish[k+1] == 0:
        mod_dish[k],mod_dish[k+1] = mod_dish[k+1],mod_dish[k]
        dish[k],dish[k+1] = dish[k+1],dish[k]

time = 0

for l in range(len(dish)):
    if l != len(dish) -1 and mod_dish[l] != 0:
        dish[l] = dish[l] + (10 - mod_dish[l])
    
    time += dish[l]

print(str(time))