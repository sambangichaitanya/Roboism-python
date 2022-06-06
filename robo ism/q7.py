x = input("Enter the no .of elements in the array:")
y = []
for i in range(int(x)):
   a = input("enter the element-" +str(i+1) + "in array:")
   y.append(a)
max = 0  
r = []  
for j in range(len(y)-1):
    count = 1
    for k in range(j+1,len(y)):
        if y[j] == y[k] :
            count += 1
            if max<=count:
                max = count
                r.append(str(y[j]))


for l in range(len(r)):
        print( str(r[l]) +" is the element in list having maximum frequency and frequency is "+str(max))