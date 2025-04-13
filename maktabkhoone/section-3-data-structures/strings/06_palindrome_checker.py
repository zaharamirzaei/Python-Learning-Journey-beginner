#کلمه palindrome
voroudi = input()
voroudi = voroudi.lower()
z=len(voroudi)
reverse=[]
for i in range(1,z+1):
    reverse.append(voroudi[-i])
reverse="".join(reverse)
if voroudi==reverse:
    print("palindrome")
else :
    print("not palindrome")
