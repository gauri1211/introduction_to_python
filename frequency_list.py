from xml.dom.minidom import Element


mylist=[]
entries=int(input("enter the no. of entries:"))
for i in range(0,entries):
    Elements_=int(input("enter the element:"))
    mylist.append(Elements_)
print(mylist)   
l1=[] 
for i in mylist:
   if i not in l1:
     l1.append(i)
   else:
    continue  
print(l1)   
#iteration,check the frequecy,print
for j in  mylist:
    frequency_=mylist.count(j)
    print("frequency_ of {}is {}".format(j,frequency_))