print("Enter 3 numbers :")
num_1 = int(input())1241
num_2 = int(input())
num_3 = int(input())
x = num_1 if num_1>num_2 else num_2
x = x if x>num_3 else num_3
print(x)
