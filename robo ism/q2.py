def function(number):
    if number.isdigit():
     a = str(number[-1])
     b = str(number[-2])
     c = str(number[-3])
     d = str(number[-4])
     e = int(len(number)-4)
     f = "*"*e
     g = str(f)
     print("your credit card number is "+g+d+c+b+a)
    else:
        print("enter valid credit card number")

num = input("Enter the credit card number :")
function(num)    