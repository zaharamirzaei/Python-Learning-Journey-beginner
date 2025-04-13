#مترجم انلاین
import collections
from typing import OrderedDict
tedad=int(input())
words=OrderedDict()
for i in range(0,tedad):
    x=input()
    x=x.split(" ")
    words[x[0]]=x[1]
sentence=input()
def translate(x):
    tarjome=list()
    y=x.split()
    for i in y:
        if i in words:
            tarjome.append(words.get(i))
        else:
            tarjome.append(i)
    tarjome= " ".join(tarjome)
    return tarjome
tarjome = translate(sentence)
print(tarjome)
