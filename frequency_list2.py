mylist=[]
entries=int(input("enter the number of entries:"))
for i in range(0,entries):
    alphabets_=input("enter the alphabets:")
    mylist.append(alphabets_)
print(mylist)
for j in mylist:
    frequency_=mylist.count(j) 
    print("frequency_ of {} is {}".format(j,frequency_))