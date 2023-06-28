#program for simple intrest
principle=int(input("enter the principle:"))
rate=float(input("enter the rate:" ))
year=int(input("enter the year:" ))
simpleintrest_=principle*rate*year*0.1
print(simpleintrest_)
#program for compound intrest
compoundintrest_=principle*(1+rate/100)*year
print(compoundintrest_)
