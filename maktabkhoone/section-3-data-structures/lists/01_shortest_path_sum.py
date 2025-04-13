#ملاقات نوروزی
#کوتاهترین مجموع مسیر طی شده

x=[]
distances=[]
for i in range(0,3):
    x.append(float(input()))
for i in range(0,3):
    first = abs(x[0]-x[i])
    second =abs(x[1]-x[i])
    third = abs(x[2]-x[i])
    distances.append(first+second+third)
distances.sort() 
kamtarin=int(distances[0])
print(kamtarin)
