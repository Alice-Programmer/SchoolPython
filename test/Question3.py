Nissu=[4,1,3,1,3,4,2,4,3]
kougeihinsu=9
Akibi=[1,1,1]
buinsu=3
for kougeihin in range(0,kougeihinsu,1):
    tantou=0
    for buin in range(1,buinsu,1):
        if Akibi[buin]<Akibi[tantou]:
            tantou=buin
    print("工芸品",kougeihin+1,"・・・","部員",tantou+1,":",Akibi[tantou],"日目~",Akibi[tantou]+Nissu[kougeihin]-1,"日目")
    Akibi[tantou]=Akibi[tantou]+Nissu[kougeihin]