#maximum age
age=int(input())
maxage= age
second= age
while age!= -1:
    age=int(input())
    if age > maxage:
        second= maxage
        maxage=age
    elif age>second :
        second=age
print(maxage,"",second)
