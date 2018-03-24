print("Numbers with all even digits between 1000 and 3000: ")
for i in range(1000,3001):
    x=str(i)
    c=0
    for t in x :
        if int(t)%2==0 :
            c+=1
    if(c==4) :
        print(i,end=", ")
        
