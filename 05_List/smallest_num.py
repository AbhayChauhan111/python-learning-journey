list=[6, 3, 9, 1, 5,34,78,33,98, 12, 45, 67, 89]
smallest=list[0]
for i in list:
    if i<smallest:
        smallest=i
print("The smallest number is:", smallest)