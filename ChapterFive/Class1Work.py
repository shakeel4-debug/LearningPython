# text="Python"
# print(text[0])
# print(text[-1])
# #Complete string
# print(text[:])
# #Revese
# print(text[::-1])
# print(text.upper())
# print(text.lower())
# print(text.capitalize())
# print(text.title())
# msg="   hello    "
# print(msg.strip())
# print(msg.lstrip())
# print(msg.rstrip())
#
# text="I love Java"
# print(text.replace("Java","Python"))
# print(text.find("Java"))
#
# #Split and joins
# data="QA,Automation,API"
# skills=data.split(",")
# print(skills)
# print("|".join(skills))
#
# text="Python123"
# print(text.isalpha())
# print(text.isdigit())
# print(text.isalnum())

count=0
name="QA is a good branch of software testing"
for ch in name:
    print(ch)
    if ch.lower()=='a':
        count+=1
print(f"Counter is ,{count}")