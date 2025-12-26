age=int(input("Enter your age"))
if age<18:
    print("You are not eligible for vote")
elif age>=18:
    citizen=bool(input("Are you citizen?"))
    if citizen:
        print("You are eligible for vote")
    else:
        print("You are not eligible for vote")