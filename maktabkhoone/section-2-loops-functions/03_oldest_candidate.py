#maximum age
age=int(input())
maxage= age
while age!= -1:
    age=int(input())
    if age > maxage:
        maxage=age
print(maxage)
