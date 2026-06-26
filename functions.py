#June-18,2026:
"""
#Task-1: Write a function that takes one number and checks whether it is even or odd using if-else.
def checker():
    print("Odd or Even Checker")
    number = int(input("Enter a number: "))
    if number%2==0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')

checker()

#Task 2: Write a function that takes a student's marks and prints: Pass if marks are 35 or above Fail if marks are below 35.
def failchecker():
    print("Pass or Fail Checker:")
    mark = float(input("Enter your marks (out of 100): "))
    if mark>=35:
        print("Passed")
    elif mark<35:
        print("Failed")
    else:
        print("Invalid Marks")

failchecker()

#Task 3: Write a function that takes a list of numbers and prints the sum of all elements.
def printlist():
    my_list = [12,45,36,42,11]
    sum = 0
    for i in my_list:
        sum+=i
    print(f"Sum of all elements in the list is {sum}")

printlist()

#Task 4: Write a function that takes a list of marks and prints the highest mark.
def highestmark():
    marks = [85,78,63,59,95]
    highest = marks[0]
    for i in marks:
        if i>highest:
            highest=i
    print("The highest mark is: ",highest)

highestmark()

#Task 5: Write a function that takes a list of names and prints each name one by one.
def displayname():
    names = ["Alex", "Bob", "Steve", "Jacob", "Emy", "Justin", "Eugene"]
    for i in names:
        print(i)

displayname()

#Task 6: Write a function that prints numbers from 1 to 10 using a loop.
def displaydigits():
    for i in range(1,11):
        print(i)

displaydigits()

#Task 7: Write a function that prints the multiplication table of 5 using a loop.
def five_table():
    for i in range(1,11):
        print(f"{i} x 5 = {i*5}")

five_table()

#Task 8: Write a function that takes a list of numbers and prints only the even numbers.
def display_onlyeven():
    my_list = [15,48,79,16,32,11]
    for i in my_list:
        if i%2==0:
            print(i)

display_onlyeven()

#Task 9: Write a function that takes a number and prints its factorial using a loop.
def display_factorial():
    number = int(input("Enter a value: "))
    factorial = 1
    for i in range(1, number+1):
        factorial *= i
    print(factorial)

display_factorial()

#Task 10: Write a function that takes a string and prints each character separately using a loop.
def display():
    x = input("Enter a string: ")
    for i in x:
            print(i)

display()
"""