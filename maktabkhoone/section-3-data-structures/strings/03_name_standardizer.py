#لیست اسامی را دریافت کند وبصورت استاندارد تحویل دهد.حرف اول اسم بزرگ و بقیه کوچک
#Convert a list of names to standardized format (Firstletter Uppercase, rest lowercas
name=[]
def standard(i):
    s=i[0]
    std= s.upper() + i[1:]
    return std
for i in range(0,10):
    a=input()
    a=a.lower()
    name.append(standard(a))
print(name)
