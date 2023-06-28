
age=int(input("enter the age:"))
if(age==0):
    print("not born yet")
elif(age>120):
    current_age=2023-age
    new_age=100-current_age
    current_year=2023+new_age
    print("you will be 100 years old in",current_year)
else:
    new_age=100-age
    current_year=2023+new_age
    print("you will be 100 years old in",current_year)
print("****know your age in a particular year****")
choice=int(input("if yes,press1 or else press0:"))
if(choice==1):
    year_=int(input("enter your year:"))
    year1=year_-2023
    new2=age+year1
    print("your age will be",new2)
else:
    print("thank you")
