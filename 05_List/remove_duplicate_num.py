list=[6, 3, 9, 1, 5, 34, 78, 33, 98, 12, 45, 67, 89,6,3,34,78,6,89]
list2=[]
for i in list:
    if i not in list2:
        list2.append(i)
print("List after removing duplicates:", list2)