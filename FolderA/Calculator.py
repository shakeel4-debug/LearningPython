print("+++Simple Calculator+++")

num1=float(input("Enter your first number:"))
num2=float(input("Enter your second number:"))

addition=num1+num2;
subtraction=num1-num2;
multiplication=num1*num2;
division=num1/num2;


print(f"{num1}+{num2}={addition}")
print(f"{num1}-{num2}={subtraction}")
print(f"{num1}*{num2}={multiplication}")
print(f"{num1}/{num2}={division:.2f}")