print("Numbers between 2000 and 3000 divisible by 7 but not 5 :")
for i in range(2000,3001):
    if i%7==0 and i%5!=0 :
        print(i,end=", ")
