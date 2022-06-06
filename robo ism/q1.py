def sorting(list,property):
    if property.lower() == "asc":
            list.sort()
            print(list)
    elif property.lower() == "desc":
            list.sort(reverse = True)
            print(list)
    elif property.lower() == "none":
            print(list)   
    else:
        print("please provide correct information.")    


list_of_numb = []
n = int(input("enter the number of elements in list:"))
for i in range(n):
    list = int(input("enter the element-"+str(i+1)+" in list:"))
    list_of_numb.append(list)

str = input("enter the property to be sorted to list as asc(for ascending)/desc(for descending)/none(for no change):")

sorting(list_of_numb,str)   