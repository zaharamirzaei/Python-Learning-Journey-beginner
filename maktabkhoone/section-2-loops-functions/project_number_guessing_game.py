import random
adad=random.randint(1,99)
voroudi=int(input("guess the number: "))
while voroudi!= adad:
    if voroudi<adad:
        print("your entered number is smaller")
    else:
        print("your entered number is bigger")
    voroudi=int(input("enter another number: "))
print("welldone its true number:",voroudi)
