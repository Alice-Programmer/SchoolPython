Akibi=[5,3,4]
buinsu=3
tantou=0
for buin in range(1,buinsu,1):
    if Akibi[buin]<Akibi[tantou]:
        tantou=buin

print("次の工芸品の担当は部員",tantou+1,"です。")