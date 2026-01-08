tools=["selenium","API","Python"]
print(tools)
print(tools[0])
print(tools[1])
print(tools[2])
print(tools[::-1])
# for tool in tools:
#     print(tool)
tools.append("Playwright")
tools.insert(1,"Cypress")
print(tools)
tools.remove("API")
tools.pop()
print(tools)
if "selenium" in tools:
    print("Yes")

print(len(tools))