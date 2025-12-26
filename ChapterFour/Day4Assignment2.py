sum=0
sum2=0
for i in range(1,101):
    if i % 2 == 0:
        sum += i
        print(i)
    else:
        sum2 += i
        print(i)

print(f"Even number {sum}")
print(f"Odd number {sum2}")