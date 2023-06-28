l1=[]
entries=int(input("enter the number of entries:"))
for i in range(0,len(entries)):
        elements=int(input("enter:"))
        l1.append(elements)
l2=[]  
print(l1)
for i in l1:
   if i not in l1:
     l2.append(i)
   else:
    continue  
print(l2)   
