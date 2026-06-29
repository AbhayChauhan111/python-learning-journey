list1=[6, 3, 9, 1, 5,34,78,33,98, 12, 45, 67, 89]
largest=list1[0]
for i in list1:
    if i>largest:
        largest=i
print("The largest number is:", largest)