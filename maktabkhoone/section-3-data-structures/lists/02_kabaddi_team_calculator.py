#مسابقات کبدی
#حداکثر تعداد تیم موردنظر
tedad= int(input())
bazi= input()
bazi=bazi.split(" ")
x=0
for i in range(0,len(bazi)):
    bazi[i]=int(bazi[i])
    if bazi[i] < 3:
        x+=1
tedadteam = x//3
print (tedadteam)
