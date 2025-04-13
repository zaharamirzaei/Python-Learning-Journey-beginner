#زیررشته AB و BA
voroudi=input()

#for i in range(0,len(voroudi)):
i=0
ab=False
ba=False
while i!= len(voroudi):
    if voroudi[i] == 'A':        
        if len(voroudi)>=i+1: 
            if voroudi[i+1]=='B':
                print("find AB")
                ab=True
                i+=2
                continue
            else :
                i+=1
                continue
        else:
            break
    if voroudi[i]== 'B':
        if len(voroudi)>=i+1:    
            if voroudi[i+1] == 'A':
                print('BA found' )
                ba=True
                i+=2
                continue
            else:
                i+=1
                continue
        else:
            break
    else:
        i+=1
if ab and ba :
    print("YES")
else :
    print("NO")
