#For loop
# for i in range(1,11):
#     print(i)

#For While loop
# i=1;
# while i<=10:
#     print(i)
#     i=i+1

#Even number 1 to 20
sum=0
for i in range(1,21):
    if i%2==0:
        sum+=i
        print(i)
    else:
        sum-=i
print(sum)
