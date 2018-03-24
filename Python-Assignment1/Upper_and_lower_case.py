print("Enter a sentence: ")
u_c =0
l_c =0
seq = input()
for x in seq :
    if x.isupper() :
        u_c+=1
    if x.islower() :
        l_c+=1
print(" UPPER CASE ",u_c," LOWER CASE ",l_c)
