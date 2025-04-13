#حروف کوچیک حروف بزرگ
voroudi=input()
def browser(a):
    low=0
    up=0
    for i in a:
        if i == i.lower():
            low+=1
        else:
            up+=1
    if up>low:
        a=a.upper()
    else:
        a=a.lower()
    return a

print(browser(voroudi))

