def doubled_string(str):
    x=[]
    y = ""
    for i in range(len(str)):
         x.append(str[i]*2)
       
    for j in range(len(x)):
            y = y + x[j]
    
    print("the doubled string is " + y)   

string = input("Enter a string: ")
doubled_string(string)