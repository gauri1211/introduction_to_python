num=int(input("enter the number:\n"))   
count=0   #initialize count to 0
for i in range(1,num+1):   #for looping till num as num>num cannot be divided
    if num%i==0:         # checking for divisibility
        count=count+1    #increamneting count if divisibility found
        continue        
if count==2:             #if count is 2 which means num is only divisible by one and itself
    print("number is prime")
else:
    print("number is not prime")
