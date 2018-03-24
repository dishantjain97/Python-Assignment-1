print("Enter a sentence: ")
seq = list(set(input().split()))
seq.sort()
print("Sorted and no duplicate words")
for word in seq:
    print(word,end=" ")
