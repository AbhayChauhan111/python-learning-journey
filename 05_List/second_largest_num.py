list=[23,56,1,34,78,56,45]
largest=float('-inf')
second=float('-inf')
for i in list:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print("Second largest number is:", second)