text="I am learning python"
reverse=""
words=text.split()
print(words)
print(len(words))
newwords="";
for word in words:
    newwords=newwords+word.capitalize()+" "
    reverse=word+" "+reverse
print(newwords)
print(reverse)