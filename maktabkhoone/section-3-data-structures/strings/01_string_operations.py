#حروف صدادار ورودی رو حذف کنه و قبل هر حرف یه نقطه بزاره
voroudi= input("please inter a word: ")
#print(type(voroudi))
voroudi= voroudi.lower()
word=""
sedadar=["a","e","o","i","u"]
for letter in sedadar:
    voroudi = voroudi.split(letter)
    voroudi = ''.join(voroudi)
for i in voroudi:
    word='.'+i+ word
print(word)
input()
