sum =0
l1=[]
while(True):
    userinput=input("please enter the price or press q:")
    
    if userinput!='q':
      sum=sum+int(userinput)

      print("sum till now:",sum)
      l1.append(userinput)
    else:
       print("bill")
       for i in l1:
          if i !='q':
           print(i)
        
    print("total",sum)
