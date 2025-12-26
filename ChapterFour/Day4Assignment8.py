a=123
c=a
b=123
reverse=0
while a>0:
    reminder=a%10
    reverse=reverse*10+reminder
    a=a//10
print(reverse)
if c==reverse:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")