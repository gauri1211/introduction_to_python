N=int(input("enter the number of apples:"))
mn=int(input("enter the starting no: "))
mx=int(input("enter the ending no: "))
if (mn==mx):
    if(N%mn==0):
        print("divisor is",mn)
else:
    for i in range(mn,mx):
        if(N%i==0):
            print("divisor is ",i)
        else:
            print("divisor is not",i)

