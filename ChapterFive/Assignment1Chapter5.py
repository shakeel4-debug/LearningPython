str="level"
reverse=""
# print(len(str))
# i=len(str)-1
# while(i>=0):
#     reverse+=str[i]
#     print(str[i])
#     i-=1
for ch in str:
    reverse=ch+reverse
print(reverse)

if str==reverse:
    print("It is a palindrome")
else:
    print("It is not a palindrome")