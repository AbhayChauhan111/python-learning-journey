
n=int(input("Enter a number:"))
    
    # return next prime number
num=n+1
while True:
       for i in range(2,num):
           if num%i==0:
               break
       else:
          print(num)
          break    
          
       num+=1
        