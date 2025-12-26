number=int(input("Enter a number: "))
if number%3==0:
    if number%5==0:
        print("You are divisible by 3 and 5")
    else:
        print("You are divisible by 3 not by 5")
else:
    print("You are not divisible by 3")