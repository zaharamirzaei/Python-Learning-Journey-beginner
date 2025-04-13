#is prime
adad=int(input())
def is_prime(x):
    javab=True
    for i in range(2,x):
        if x%i==0:
            javab=False
    return javab    
        
        
javab=is_prime(adad)
if javab:
    print(" prime")
else:
    print("not prime")
