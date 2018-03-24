print("Enter a sentence: ")
seq = input().split()
seq.sort()
print("The words sorted in an alphabetic order are: ")
for word in seq :
    print(word)
