item=input("enter the item")
rev=""
for i in item:
    rev=i+rev
print(rev)

if item==rev:
    print("palindrome")
else:
    print("not palindrome")

# def isPalindrome(str):
 
#     # # Run loop from 0 to len/2
#     # for i in range(0, int(len(str)/2)):
#     #     if str[i] != str[len(str)-i-1]:
#     #         return False
#     # return True
 
