list=[6, 3, 9, 1, 5,34,78,33,98, 12, 45, 67, 89]
even=0
odd=0
for i in list:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Total even numbers are:",even)
print("Total odd numbers are:",odd)