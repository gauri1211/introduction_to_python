l1=['a','e','i','o','u']

item=input("enter the string:")
count=0
for i in item:
    if i in l1:
        count+=1
        continue
print("the no of vowels are",count)
