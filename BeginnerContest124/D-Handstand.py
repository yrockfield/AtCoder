# -*- coding: utf-8 -*-

# スペース区切りの整数の入力
n, k = map(int, input().split())

# 01文字列の入力
s = str(input())

sakaMax = 0

for a in range (2):
    if a == 0:
        # 01文字列を配列に一文字ずつ格納
        hito = list(s)
        sakaCnt = 0
        irekae = 0
        prevIsZero = False
        startIndex = 0
    else:
        # 01文字列を配列に一文字ずつ格納
        hito = list(s)
        # 2回目は逆順にして後ろからやってみる
        hito.reverse()

        sakaCnt = 0
        irekae = 0
        prevIsZero = False
        startIndex = 0

    tmp01Cnt = 0
    max01Cnt = 0
    # 0 or 1が続いて出現するところを探す
    tmp01 = hito[0]
    kirikae = 0
    for h in range(1,len(hito)):
        tmp01Cnt=0
        for g in range(h,len(hito)):
            if tmp01 == hito[h]:
                tmp01Cnt += 1
                if tmp01Cnt > max01Cnt:
                    max01Cnt = tmp01Cnt
                    startIndex = h-tmp01Cnt
            else:
                tmp01Cnt += 1
                # 0 -> 1 に切り替わったらインクリメント
                if tmp01 == 0:
                    kirikae += 1
                else:
                    if kirikae >= k:
                        break
                # # 1 <-> 0 の切り替わりが(k)回超えたらまた0からカウント
                # if kirikae > k * 2 :
                #     tmp01Cnt = 0
                #     kirikae = 0
                tmp01 = hito[h]

            if h == len(hito)-1 and  tmp01Cnt > max01Cnt:
                max01Cnt = tmp01Cnt
                startIndex = h-tmp01Cnt
        if tmp01Cnt > max01Cnt:
            max01Cnt = tmp01Cnt
        tmp01Cnt = 0

    print ("max01Cnt:{}".format(str(max01Cnt)))

    # # とりあえず頭から0を1に変換してみる
    # for i in range(len(hito)):
    # 0 or 1が続いて出現するところ以降でやってみる
    for i in range(startIndex, len(hito)):
        if hito[i] == "1":
            if prevIsZero == True:
                irekae += 1
                prevIsZero = False
        else:
            if irekae < k:
                hito[i] = "1"
            if prevIsZero == False:
                prevIsZero = True

    prevIsZero = False
    for j in range(len(hito)):
        # print ("hito[{}]:{}".format(str(j),hito[j]))
        if hito[j] == "1":
            sakaCnt += 1
        else:
            if sakaMax < sakaCnt:
                sakaMax = sakaCnt
            sakaCnt = 0

    if sakaMax < sakaCnt:
        sakaMax = sakaCnt

# 出力
print(sakaMax)        
