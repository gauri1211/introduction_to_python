def fact(n):
    if n<0:
        print("negetive number")
    elif n==0:
        return 1
    else:
        for i in range(1,n):
            n=n*i
    return n
def trailingzero(n):
    count=0
    f=fact(n)
    while(f%10==0):
        count+=1
        n=n/10
n=int(input("enter:"))
print(fact(n))
print(trailingzero(n))
