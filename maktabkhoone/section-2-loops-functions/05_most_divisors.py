#MAGHSOOM
def maghsoom(x):
    tedad=1
    for i in range(2,x):
       if x%i==0:
           tedad=tedad+1
    return tedad
a=0
finallnum=0
for j in range(0,20):
    adad=int(input())
    b=maghsoom(adad)
    if b > a :
        a=b
        finallnum=adad
    elif b==a :
        if adad > finallnum:
            finallnum=adad

print(finallnum,"",a)
