# -*- coding: utf-8 -*-

# 整数の入力
x,y,z,k = map(int,input().split())

# cakea,b,cのおいしさをリストに取得
cakea = list(map(int, input().split()))
cakeb = list(map(int, input().split()))
cakec = list(map(int, input().split()))

# ケーキリストをおいしい順にソートしておく
cakea.sort(reverse=True)
cakeb.sort(reverse=True)
cakec.sort(reverse=True)

oishisa = []

# # おいしそうなケーキ候補リスト
# sela = []
# selb = []
# selc = []

# # a,b,cから一つずつ、一番おいしいのを候補リストに入れる
# sela.append(cakea[0])
# selb.append(cakeb[0])
# selc.append(cakec[0])
# # 候補リストに入れたらケーキリストから削除しておく
# del cakea[0]
# del cakeb[0]
# del cakec[0]

# while len(sela) * len(selb) * len(selc) < k:
#     # a,b,c のうちおいしそうな順番で候補リストに追加していく
#     if len(cakea)>0:
#         tmpCakeA = cakea[0]
#     else:
#         tmpCakeA = -1

#     if len(cakeb)>0:
#         tmpCakeB = cakeb[0]
#     else:
#         tmpCakeB = -1
#     if len(cakec)>0:
#         tmpCakeC = cakec[0]
#     else:
#         tmpCakeC = -1

#     if tmpCakeA > tmpCakeB and tmpCakeA > tmpCakeC:
#         sela.append(tmpCakeA)
#         del cakea[0]
#     elif tmpCakeB > tmpCakeA and tmpCakeB > tmpCakeC:
#         selb.append(tmpCakeB)
#         del cakeb[0]
#     elif tmpCakeC > tmpCakeA and tmpCakeC > tmpCakeB:
#         selc.append(tmpCakeC)
#         del cakec[0]
#     elif tmpCakeA == tmpCakeB :
#         if tmpCakeA > tmpCakeC:
#             sela.append(tmpCakeA)
#             del cakea[0]
#         else:
#             selc.append(tmpCakeC)
#             del cakec[0]
#     elif tmpCakeA == tmpCakeC:
#         if tmpCakeA > tmpCakeB:
#             sela.append(tmpCakeA)
#             del cakea[0]
#         else:
#             selb.append(tmpCakeB)
#             del cakeb[0]
#     elif tmpCakeB == tmpCakeC:
#         if tmpCakeA > tmpCakeB:
#             sela.append(tmpCakeA)
#             del cakea[0]
#         else:
#             selb.append(tmpCakeB)
#             del cakeb[0]
#     elif tmpCakeA == tmpCakeB and tmpCakeA == tmpCakeC:
#         sela.append(tmpCakeA)
#         del cakea[0]

# print ("sela:{},selb:{},selc:{}".format(sela,selb,selc))

# 全部回すと時間かかりすぎ
# でも全部回す必要があるときはそうする
if x*y*z == k:
    for a in range(len(cakea)):
        for b in range(len(cakeb)):
            for c in range(len(cakec)):
                oishisa.append(cakea[a] + cakeb[b] + cakec[c])
else:
    idx_a = 0
    idx_b = 0
    idx_c = 0
    whichismax=[]

    while len(oishisa) < k:
        if len(oishisa)>0:
            # a,b,cのどのインデックスを進めるか
            whichismax.clear()
            if len(cakea)>idx_a+1:
                whichismax.append(cakea[idx_a+1] + cakeb[idx_b] + cakec[idx_c])
            else:
                whichismax.append(-1)
            
            if len(cakeb)>idx_b+1:
                whichismax.append(cakeb[idx_b+1] + cakea[idx_a] + cakec[idx_c])
            else:
                whichismax.append(-1)
                
            if len(cakec)>idx_c+1:
                whichismax.append(cakec[idx_c+1] + cakea[idx_a] + cakeb[idx_b])
            else:
                whichismax.append(-1)
            
            if whichismax.index(max(whichismax)) == 0:
                idx_a += 1
            elif whichismax.index(max(whichismax)) == 1:
                idx_b += 1
            elif whichismax.index(max(whichismax)) == 2:
                idx_c += 1

        print(whichismax)
        print ("idx_a:{},idx_b:{},idx_c:{}".format(idx_a,idx_b,idx_c))
        oishisa.append(cakea[idx_a] + cakeb[idx_b] + cakec[idx_c])

# for a in range(x):
#     for b in range(y):
#         for c in range(z):
#             oishisa.append(cakea[a] + cakeb[b] + cakec[c])

oishisa.sort(reverse=True)

for i in range(k):
    print(oishisa[i])