from xml.dom.minidom import Element


l1=[]
num=int(input("enter the number of entries:"))

for i in range(0,num):
    name_ =input("enter name:")
    l1.append(name_)

print(l1)

obj_=input("enter the Element:")
if obj_ in l1:
  l1.remove(obj_)
else:
    print("invalid element not present in list")
print(l1)