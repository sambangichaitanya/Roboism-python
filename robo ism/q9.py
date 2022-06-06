d = []
a = input("Enter a string:")
for i in range(len(a)):
    d.append(a[i])

d.sort()
sum=""
for j in range(len(d)):
    sum += d[j]

print(sum)    