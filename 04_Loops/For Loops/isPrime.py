n=int(input("Enter a number:"))
if n<=1:
    print("Not a prime number")
for i in range(2,n):
    if n%i==0:
        print("Not a prime number")
        break
    else:
        print("It is a prime number")
        break