#سارا سلام میکنه
s= list(input())
hello="hello"
a=0
for i in s:
    #harf=s.pop()
    if i==hello[a]:
        a=a+1
    if a==5:
        print("YES")
if a<5 :
    print("NO")
