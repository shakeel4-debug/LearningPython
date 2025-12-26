# Number is prime or not
star=4
end=100
isPrime=True
for i in range(star,end):
    for j in range(2,i-1):
        if i%j==0:
            isPrime=False
            break
    



