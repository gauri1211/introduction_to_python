mylist=[]
entries = int(input("enter the number of entries:"))
for i in range(0,entries):
   price=float(input("enter the price:"))
   mylist.append(price)
print(mylist)
total= 0
for j in range(0,len(mylist)):
    total=total+mylist[j]
print(total)
discount_=0.3*total

print(discount_)