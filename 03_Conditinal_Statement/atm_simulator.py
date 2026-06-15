balance = 5000
pin = 1234

entered_pin = int(input("Enter PIN: "))

if entered_pin == pin:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Change Pin")
    print("5. Fast Cash")
    print("6. Exit")
    print("====================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("your remaining balance is :", balance)
    elif choice == 2:
        withdraw=int(input('Enter withdrawn amount:'))
        if withdraw <=0:
            print("Invalid Amount")
        elif withdraw > balance:
               print("Insufficient Balance")
 
        else:
            balance=balance-withdraw
            print(withdraw,"amount has been withdrawn")
            print("Remaining amount is:", balance)
    elif choice ==3:
        deposit=int(input("Enter deposit money:"))
        if deposit <=0:
            print("Invalid anount")
        else:
            balance=balance+deposit
            print("Your current balance is:",balance)
    elif choice ==4:
        curr_pin=int(input("Enter your current pin:"))
        if curr_pin==pin:
            new_pin=int(input("Enter new pin:"))
            pin=new_pin
            print("pin has been changed:")
        else:
            print("Invalid pin")
    elif choice ==5:
        print("Select amount fro fast withdraw:")
        print("1. 100")
        print("2. 500")
        print("3. 1000")
        amt= int(input("Enter your choice: "))
        

        if amt ==1:
            if balance>=100:
                 balance=balance-100
                 print("Amount 100 withdrawn successfully!")
                 print("Remaining balance is:",balance)
            else:
                print("Insufficient Balance!")
           
        elif amt==2:
            if balance>=500:
                balance=balance-500
                print("Amount 500 withdrawn successfully!")
                print("Remaining balance is:",balance)
            else:
                print("Insufficient Balance!")
            
        elif amt==3:
            if balance>=1000:
                 balance=balance-1000
                 print("Amount 1000 withdrawn successfully!")
                 print("Remaining balance is:",balance)
            else:
                print("Insufficient Balance!")
           
        else:
            print("Invalid Choice!")
        
    elif choice ==6:
        print("Thank you for using ATM!")

else:
    print("Invalid PIN")
