def operation(a,b,c):
        a = float(a)
        c = float(c)
        if b == '+':
          print(a + c)
        elif b == '-':
          print(a-c)
        elif b == '*':
          print(a*c)
        elif b == '/':
          print(a/c)
        else :
          print("syntax error!")


a = input("enter the first number: ")
b = input("enter the operation: ")
c = input("enter the second number: ")
operation(a,b,c)