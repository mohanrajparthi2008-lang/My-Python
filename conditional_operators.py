#May-13,2026
#Conditional Operator
a = True 
b = False 
c = False 
d = True
print(a and b) or (not (c or d) and (a == b))
print((a or b) and (c == d)) or (not (a == c))
print((a == b or c < d) and (a != d or b > c))
print(a and (b or c)) and not (d or (b and c))
print(a and b and c) or not (d and (a == b))
print(not(a or (b and c) or (d == True)) and (a or b))
print(a == d or (b and c) and not (a != b))
print((a and b) or (c > d)) and not (a == c) and (b != c)
print((a and b) or (c == d)) and not (a != d) and (c < b)
print(a or (b and not c) or (d == True)) and not (a == b and c != d)
print(not(a and b) or (c < d and (b == False or d == True)))
print(not(a or b) and (c <= d or not (a == b)) and (c == b))
print(a and (b or c)) or not (a == b) and (c != d)
print(a == True and b == False) or not (c == d) and (a or d)
print((a == b) or not (c <= d)) and ((b or c) and (a != d))
print(a or (b and (c <= d))) or not (a == c and d != True)
print(not (a and (b or (c and d))) or (c == b and (a == d)))
print(a and (b == False or c == True)) and not (d and b)
print(a or (b and (c or d))) and not (a == c or b != d)
print((a and b) or (c and d)) and not (a == c and b != d) or (a == d)
print(not(a and b) and (c != d) or (a == b and not (c == d)))
print((a or b) and (c == True)) or (a == d and not (c != b))
print((a and b) or not (c == True)) and (a == b or (c < d))
print(a or (b and not (c == d))) and (a != d or not (b == False))
print((a == d and not (b and c)) or (a != c and b == True)) and (c != d)
print((a or (b and c)) and d == True) or not (a == c)
print(a and not (b or c) and (d == True)) or not (a and b)
print((a and b) or ((c == True) and (d != False))) and not (a == b)
print(a == b and not (c and d)) or (a != d and c == b)
print((a == b and c != d) or not (a and c)) and (a or (b and d))

#May-15, 2026
#if-elif-else
n = float(input("Enter number to check whether positive or negative:"))
if(n==0):
    print("Your number is zero")
elif(n<0):
    print("Your number is negative")
else:
    print("Your number is positive")

x = float(input("Enter your marks to check your grade:"))
if(x>90):
    print("You have passed the exam and received A grade")
elif(75<x<89):
    print("You have passed the exam and received B grade")
elif(50<x<74):
    print("You have passed the exam and received C grade")
elif(35<=x<49):
    print("You have passed the exam and received D grade")
else:
    print("You have failed the exam and received E grade")
    
y = int(input("Enter a value to check divisibility by 2 and 3:"))
if(y%2==0 and y%3==0):
    print("The number is divisible by both 2 and 3")
elif(y%2==0):
    print("The number is divisible by 2")
elif(y%3==0):
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 2 or 3")

a = float(input("Enter a value for A:"))
b = float(input("Enter a value for B:"))
choice = int(input("Enter 1 to add, Enter 2 to subtract, Enter 3 to multiply, Enter 4 to divide:"))
if(choice==1):
    print(f"The answer is {a+b}")
elif(choice==2):
    print(f"The answer is {a-b}")
elif(choice==3):
    print(f"The answer is {a*b}")
elif(choice==4):
    if(b!=0):
        print(f"The answer is {a/b}")
    else:
        print(f"The answer is undefined")
else:
    print("Invalid choice")
