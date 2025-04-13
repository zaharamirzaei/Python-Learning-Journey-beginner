#شمارش ارا
kole_ara=int(input())
ara=list()
for i in range(0,kole_ara):
    ara.append(input())
ara.sort()
finall_ara=dict()
for name in ara:
    if name in finall_ara:
        finall_ara[name] +=1
    else:
        finall_ara[name] = 1
#print(finall_ara)        
#listkeshvar= list(finall_ara).sort()
#print(listkeshvar)
for i in list(finall_ara.keys()):
    print('%s %s' %(i,finall_ara[i]))
    
