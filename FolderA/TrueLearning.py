# print("Python code is called and clean")
#
# if True:
#     print("This line is indented")
#     print("This line is also indented")
# print("This line is back to main level")
#
# def greet(name):
#     print(f"Hello, {name}")
#     print(f"Welcome to python!")
#
# greet("Programmer")

"""
print("====INDENtatION EXAMPLE====")
name="Alice"
age=25

if age>=18:
    print(f"{name} is an adult")
    print("They can vote")
    if age>=21:
        print("They can also drink")


print("Back to main level (no indentation)")
"""

# age=int(input("Enter you age:"))
# if 0<=age<=120:
#     print("Valid age enterted")
#     birth_year=2024-age
#     print(f"You were probabaly born in {birth_year}")
# else:
#     print ("Please enter a realistic age")


first="Hello"
second="World"
print(f"Before swappping {first},{second}")

first,second=second,first
print(f"After swapping{first},{second}")