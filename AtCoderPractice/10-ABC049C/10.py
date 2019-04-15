# -*- coding: utf-8 -*-
import re

# 文字列入力
n = input()

patern="^(dream|dreamer|erase|eraser)+$"

if re.match(patern,n):
        print ("YES")
else:
        print ("NO")

