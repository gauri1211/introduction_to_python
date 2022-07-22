#with for loop

'''
for i in range(1,56):
    if i%3==0 and i%5==0 and i%10!=0:
        print(i,end=" ")
    else:
        continue
    '''

#with while loop

i=1
while(i<56):
    if i%3==0 and i%5==0 and i%10!=0:
        print(i,end=" ")
        i+=1
    else:
        i+=1
        continue