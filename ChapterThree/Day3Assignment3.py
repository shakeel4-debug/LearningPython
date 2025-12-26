age=int(input("Enter your age:"))
if age<18:
    print ("You are minor")
elif age>=18 and age<59:
    print("You are adult")
elif age>=59:
    print("You are senior")