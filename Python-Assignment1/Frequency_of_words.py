print("Enter a sentence: ")
seq = input().split()
count=dict()
for word in seq:
    if word in count :
        count[word]+=1
    else :
        count[word]=1
for word in sorted(count):
    print(word,":",count[word])
    
