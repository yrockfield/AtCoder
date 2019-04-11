# -*- coding: utf-8 -*-

# 3桁の整数の入力
s = input()
s1,s2,s3 = s[:1], s[1:2], s[2:]

print(int(s1) + int(s2) + int(s3))
