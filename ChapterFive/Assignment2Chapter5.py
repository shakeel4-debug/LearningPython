counter=0
sentence="a quick brown fox jumped over the lazy dog"
for ch in sentence:
    if ch.lower()=='a' or ch.lower()=='e' or ch.lower()=='i' or ch.lower()=='o' or ch.lower()=='u':
        counter+=1
print(f"Vowels: {counter}")