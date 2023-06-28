entries=int(input("enter the no of entries"))

l1=[]
for i in range(0,entries):
    temp=int(input("enter the item\n"))
    l1.append(temp)
print(l1)
sum=0
for j in l1:
    if j%2==0:
        sum+=j
        continue
print(sum)
 