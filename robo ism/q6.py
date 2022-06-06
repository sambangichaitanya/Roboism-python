a=int(input("Enter the lower limit:"))
b=int(input("Enter upper limit: "))
if a>b:
    temp = a
    a = b
    b = temp
    
for c in range(a,b):
    k=0
    for i in range(2,c//2+1):
        if(c%i==0):
            k=k+1
    if(k<=0):
        print(c)