#May-19, 2026
units = int(input("Enter the units of your electricity bill:"))
if(units<0):
    print("invalid units")
    
else:
    if(units<=100):
        bill = (units*5)
    elif(units<=200):
        bill = ((units-100)*7)+(100*5)
    else:
        bill = (100*5)+(100*7)+((units-200)*10)
    if(bill>2000):
        final=bill+(bill*0.1)
        print(f"Total amount= {final} rupees")
    else:
        print(f"Total amount= {bill} rupees")

print("Welcome to World Bank")
a = 10000
x = int(input("Enter 3 to check balance, Enter 2 to deposit funds, Enter 1 to withdraw funds:"))
if(x==1):
    y = int(input("Enter the amount to withdraw:"))
    if(y<=10000):
        print(f"You have withdrawn {y} rupees. Your remaining balance is {a-y} rupees")
    else:
        print("Insufficient balance")
elif(x==2):
    y = int(input("Enter the amount to deposit:"))
    print(f"You have deposited {y} rupees. Your new balance is {a+y} rupees")
elif(x==3):
    print(f"Your current balance is {a} rupees")
else:
    print("Invalid choice")

db_username = "user01"
db_password = "1234"
email = input("Enter your email:")
password = input("Enter your password:")
if (email!=" " and password!=" "):
    if (email == db_username):
        if (password == db_password):
            print("Login successful")
        else:
            print("Invalid password")
    else:
        print("User not found")
else:
    print("Email and password cannot be empty")
    
print("ATM Withdrawal System")
db_pin = 1234
account_balance = int(input("Enter your account balance:₹"))
withdrawal_amount = int(input("Enter the amount to withdraw:₹"))
pin = int(input("Enter your 4-digit PIN:"))
if(pin==db_pin):
    if(withdrawal_amount<=account_balance):
        if(withdrawal_amount%100==0):
            print(f"Please collect your cash: ₹{withdrawal_amount}")
            print(f"Your remaining balance is: ₹{account_balance-withdrawal_amount}")
        else:
            print("Invalid denomination. Please enter an amount in multiples of 100.")
    else:
        print("Insufficient balance")
else:
    print("Invalid PIN")

print("Online Shopping Discount")
amount = float(input("Enter the purchase amount of your shopping:₹"))
membership = input("Are you a member of our online shopping club? (yes/no):")
if(amount>5000):
    if(membership=="yes"):
        print("Congratulations! You are eligible for a 20% discount on your purchase.")
        print(f"Your total amount is:₹{amount*0.8}" )
    else:
        print("Congratulations! You are eligible for a 10% discount on your purchase.")
        print(f"Your total amount is:₹{amount*0.9}" )
elif(amount>2000):
    if(membership=="yes"):
        print("Congratulations! You are eligible for a 10% discount on your purchase.")
        print(f"Your total amount is:₹{amount*0.9}" )
    else:
        print("Congratulations! You are eligible for a 5% discount on your purchase.")
        print(f"Your total amount is:₹{amount*0.95}" )
else:
    print("Sorry, you are not eligible for a discount on your purchase.")
    print(f"Your total amount is:₹{amount}" )    
