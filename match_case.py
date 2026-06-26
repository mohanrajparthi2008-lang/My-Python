#May-20, 2026
print("Odd or Even Checker")
a = float(input("Enter a value: "))
match a:
    case u if u % 2 == 0:
        print(f"{a} is an even number.")
    case _:
        print(f"{a} is an odd number.")

print("Positive or Negative Calculator")
number = float(input("Enter a number: "))
match number:
    case n if n > 0:
        print("The number is positive.")
    case n if n < 0:
        print("The number is negative.")
    case _:
        print("The number is zero.")

print("Welcome to Simple Calculator")
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
print("Select the operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice (1/2/3/4):"))
match choice:
    case 1:
        print(f"The result of addition is: {a+b}")
    case 2:
        print(f"The result of subtraction is: {a-b}")
    case 3:
        print(f"The result of multiplication is: {a*b}")
    case 4:
        if b != 0:
            print(f"The result of division is: {a/b}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid choice. Please select a valid operation.")

day = input("Enter the day of the week:")
match day:
    case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
        print("It's a weekday.")
    case "Saturday"|"Sunday":
        print("It's the weekend.")
    case _:
        print("Invalid day entered.")

print("Grading system")
marks = float(input("Enter your marks to check your grade:"))
match marks:
    case x if x > 90:
        print("You have passed the exam and received A grade")
    case x if 75 < x < 89:
        print("You have passed the exam and received B grade")
    case x if 50 < x < 74:
        print("You have passed the exam and received C grade")
    case x if 35 <= x < 49:
        print("You have passed the exam and received D grade")
    case _:
        print("You have failed the exam and received E grade")

month = input("Enter the month (1-12): ")
match month:
    case "1":
        print("January")
    case "2":
        print("February")
    case "3":
        print("March")   
    case "4":
        print("April") 
    case "5":
        print("May")
    case "6":
        print("June")
    case "7":
        print("July")
    case "8":
        print("August")
    case "9":
        print("September")
    case "10":
        print("October")
    case "11":
        print("November")
    case "12":
        print("December")
    case _:
        print("Invalid month")

print("Vowel or Consonant Checker")
letter = input("Enter a letter: ")
match letter:
    case "a" | "e" | "i" | "o" | "u":
        print("The letter is a vowel.")
    case _:
        print("The letter is a consonant.")

print("Traffic light color:")
color = input("Enter the traffic light color (red, yellow, green): ")
match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid traffic light color")

print("Leap Year Checker")
year = int(input("Enter a year: "))
match year:
    case y if y % 4 == 0:
        print(f"{year} is a leap year.")
    case _:
        print(f"{year} is not a leap year.")

print("Age group classification:")
age = int(input("Enter your age: "))
match age:
    case age if 0 <= age <= 12:
        print("You are a child.")
    case age if 13 <= age <= 19:
        print("You are a teenager.")
    case age if 20 <= age <= 59:
        print("You are an adult.")
    case age if age >= 60:
        print("You are a senior citizen.")
    case _:
        print("Invalid age entered.")

num = int(input("Enter a number from 1 to 10: "))
match num:
    case 1:
        print("You entered one.")
    case 2:
        print("You entered two.")
    case 3:
        print("You entered three.")
    case 4:
        print("You entered four.")
    case 5:
        print("You entered five.")
    case 6:
        print("You entered six.")
    case 7:
        print("You entered seven.")
    case 8:
        print("You entered eight.")
    case 9:
        print("You entered nine.")
    case 10:
        print("You entered ten.")
    case _:
        print("Invalid input. Please enter a number from 1 to 10.")

print("Shape identifier")
side = input("Enter the number of sides of the shape: ")
match side:
    case "3":
        print("The shape is a triangle.")
    case "4":
        print("The shape is a quadrilateral.")
    case "5":
        print("The shape is a pentagon.")
    case "6":
        print("The shape is a hexagon.")
    case "7":
        print("The shape is a heptagon.")
    case "8":
        print("The shape is a octagon.")
    case "9":
        print("The shape is a nonagon.")
    case "10":
        print("The shape is a decagon.")
    case "11":
        print("The shape is a hendecagon.")
    case "12":
        print("The shape is a dodecagon.")
    case _:
        print("Shape not identified.")

number = float(input("Enter a number: "))
match number:
    case n if n%3 == 0 and n%5 == 0:
        print(f"{number} is divisible by both 3 and 5.")
    case n if n%3 == 0:
        print(f"{number} is divisible by 3.")
    case n if n%5 == 0:
        print(f"{number} is divisible by 5.")
    case _:
        print(f"{number} is not divisible by 3 or 5.")

num = float(input("Enter a number: "))
match num:
    case n if n > 0 and n % 2 == 0:
        print("The number is positive and even.")
    case n if n > 0:
        print("The number is positive and odd.")
    case 0:
        print("The number is zero.")
    case _:
        print("The number is negative.")
