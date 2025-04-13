#مقایسه قیمت لپتاپ ها

tedad=int(input())
details=[]
happy=False
for i in range(0,tedad):
    details.append(input())
details.sort()
def compare(tedad,details):
    for i in range(0,tedad):
        a=details[i].split()
        for n in range(i+1,tedad):
            b=details[n].split()
            if a[0]<b[0]:
                if a[1]>b[1]:
                    happy=True
                    #print("happy")
                    break
                else:
                    continue
        if happy:
            break
    return happy
x=compare(tedad,details)        
if x:
    print("happy")
else:
    print("poor")  
