a = input("Enter a string:")
sum = 0        
for i in range(len(a)):
    if a[i].isdigit():
        sum += int(a[i])
    
print(sum)