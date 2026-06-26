#May-25,2026
"""       
#Task 1: Print numbers from 0 to 10
for x in range(1,11):
    print (x)

#Task 2: Print even numbers from 0 to 20
for x in range(21):
    if x % 2 == 0:
        print(x)

#Task 3: Print odd numbers from 1 to 20
for n in range(1, 21, 2):
    print(n)

#Task 4: Print numbers from 10 to 1 in reverse order.
for p in range(10, 0, -1):
    print(p)

#Task 5: Print the square of each number from 1 to 10
for i in range(1, 11):
    i**=2
    print(i)
    
#Task 6: Print the multiples of 5 up to 50
for i in range(1, 11):
    print(f"{i} x 5 = {5 * i}")

#Task 7: Calculate the sum of numbers from 1 to 10
add = 0
for i in range(1, 11):
    add += i
print(add)

#Task 8: Calculate the sum of even numbers from 1 to 20
add = 0
for i in range(2,21,2):
    add += i
print(add)

#Task 9: Calculate the sum of odd numbers from 1 to 20
add = 0
for i in range(1, 21, 2):
    add += i
print(add)

#Task 10: Program to print the multiplication table of 7
for i in range(1, 11):
    print(f"{i} x 7 = {7 * i}")

#Task 11: Print numbers divisible by 3 from 1 to 100
for n in range(101):
    if n % 3 == 0:
        print(n)

#Task 12: find the factorial of 5 using a for loop
f = 1
for i in range(1, 6):
    f *= i
print(f)
        
#Task 13: Print numbers from 1 to a user input number
n = int(input("Enter a number: "))
for i in range(1, n + 1, 1):
    print(i)
"""
#May-26,2026
"""
#Task 14: Program to count digits using a for loop
n = input("Enter a number: ")
digit = 0
for i in n:
    digit = digit + 1
print(digit)

#Task 15: Program to reverse a number using a for loop
n = input("Enter a number: ")
reverse = ""
for i in n:
    reverse = i + reverse
print(reverse)

#Task 16: Program to print the digits of a number using a for loop
n = input("Enter a number: ")
for i in n:
    print(i)

#Task 17: Program to find the sum of digits of a number 
n = int(input("Enter a number: "))
total = 0
for i in str(n):
    total += int(i)
print(total)

#Task 18: Program to calculate power of a number using a for loops
a = int(input("Enter the base: "))
p = int(input("Enter the exponent: "))
r = 1
for i in range(p):
    r *= a
print(r)

# Task 19: Program to check if a number is prime or not using a for loop
n = int(input("Enter a number: "))
if n <= 1:
    print(f"{n} is not a prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is a prime number")

#Task 20: Program to print a right-triangle pattern of stars
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print("*" * i)
"""
#May-27,2026
"""
#Task 1: Program to print numbers from 1 to 10 using a while loop.
i = 1
count = 10
while i<=count:
    print(i)
    i+=1

#Task 2: Program to print even numbers from 1 to 20 using a while loop.
i = 2
count = 20
while i<=count:
    print(i)
    i+=2

#Task 3: Program to print odd numbers from 1 to 20 using a while loop
i = 1
count = 20
while i<=20:
    print(i)
    i+=2

#Task 4: Program to print numbers from 10 to 1 in reverse order
x=10
while x>=1:
    print(x)
    x-=1

#Task 5: Program to print numbers from 1 to n using a while loop
n = int(input("Enter a number: "))
count = 1
while count<=n:
    print(count)
    count +=1

#Task 6: Program to print the multiples of 5 up to 50 using while loop
i = 5
count = 50
while i<=count:
    print(i)
    i+=5

#Task 7: Program to find the sum of numbers from 1 to 10.
add = 0
number = 1
count = 10
while number <= count:
    add += number  
    number += 1          
print(add)

#Task 8: Program to find the sum of even numbers from 1 to 20.
add = 0
number = 2
count = 20
while number <= count:
    add += number  
    number += 2          
print(add)

#Task 9: Program to find the sum of odd numbers from 1 to 20.
add = 0
number = 1
count = 20
while number <= count:
    add += number  
    number += 2          
print(add)

#Task 10: Program to print the multiplication table of 7
n = 1
while n <= 10:
    result = 7 * n
    print(f"7 x {n} = {result}")
    n += 1
"""
#June-1,2026
"""
#Right Angled Triangle Pattern
n = int(input("Enter the row size for the pattern: "))
for i in range(n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

#Inverted Right Angled Triangle
rows = int(input("Enter the row size for the pattern: "))
for i in range(rows, 0, -1):
    for j in range(i + 1):
        print("*", end=" ")
    print()

#Pyramid Pattern
r = int(input("Enter the row size for the pattern: "))
for i in range(r+1): 
    for j in range(r-i):  
        print(" ", end=" ")
    for k in range(2 * i):
        print("*", end=" ")
    print()

#Inverted Pyramid Pattern
x = int(input("Enter the row size for the pattern: "))
for i in range(x , 0, -1):
    for j in range(x  - i):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print("*", end=" ")
    print()
#Alternate:
x = int(input("Enter the row size: "))
for i in range(x, 0, -1):
    spaces = " " * (x - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

#Diamond Pattern
rows = int(input("Enter the row size for the pattern: "))
for i in range(1,rows + 1):
    for j in range(rows  - i):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print("*", end=" ")
    print()
for i in range(rows  - 1, 0, -1):
    for j in range(rows  - i):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print("*", end=" ")
    print()
"""
#June-2,2026: Class
"""
courseName = "Python Programming"
print(len(courseName),"length")
print(courseName.upper(),"uppercase")
print(courseName.lower(),"lowercase")
print(courseName.casefold())
print(courseName.capitalize())
print(courseName.count("a"))
print(courseName.center(50))
print(courseName.index("y"))
print(courseName.index("g"))
print(courseName[0:6])
print(courseName[7:])
print(courseName[:10])
for i in courseName:
    print(i)
name = "     demoname     "
print(name)
print(name.strip()) 
print(name.lstrip()) 
print(name.rstrip())
replacedValue = courseName.replace("Python","Java")
print(replacedValue,"replacedValue")
print("mithra".isalpha())
print("mi#hfdjf".isalpha())
print(courseName.endswith("g"))
print(courseName.endswith("m"))
print(courseName.endswith("G"))
print(courseName.startswith("p"))
print(courseName.startswith("P"))
"""

#June-2,2026: Home
"""
#Task-1: Write a program to count the number of vowels in a given string.
n = input("Enter a string: ")
count = 0
for i in n:
    if i in "aeiouAEIOU":
        count+=1
print(count)

#Task-2: Program to reverse a string using a loop (without using slicing).
n = input("Enter a string: ")
reverse = ""
for i in n:
    reverse = i + reverse
print(reverse)

#Task-3: Program to check if a string is a palindrome
r = input("Enter a string: ")
reverse = ""
for i in r.lower():
    reverse = i + reverse 
if r.lower() == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

#Task-4: Write a program to count the number of uppercase and lowercase letters in a given string.
s = input("Enter a string: ")
upper = 0
lower = 0
for i in s:
    if 'A' <= i <= 'Z':
        upper += 1
    elif 'a' <= i <= 'z':
        lower += 1
    else:
        pass
print(f"Number of uppercase letters: {upper}")
print(f"Number of lowercase letters: {lower}")

#Task-5: Program to remove all spaces from a given string using a loop.
x = input("Enter a string: ")
no_spaces = ""
for i in x:
    if i != " ":
        no_spaces += i
print(no_spaces)

#Task-6: Program to find the frequency of each character in a string.
x = input("Enter a string: ")
lower = x.lower() 
seen = "" #to keep track of characters we've already counted
for i in lower:
    if i not in seen:
        count = lower.count(i)
        print(f"Frequency of '{i}': {count}")
        seen += i   

#Task-7: Program to count the number of numeric characters in a given string
n = input("Enter a string: ")
numeric_count = 0
for i in n:
    if i.isnumeric():
        numeric_count += 1
print(f"Total numeric characters: {numeric_count}")

#Task-8: Program to check if a given string contains only alphabets (both uppercase and lowercase).
x = input("Enter a string: ")
y = x.lower()
alphabet = True
for i in y:
    if not ("a" <= i <= "z"):
        alphabet = False
        break
if alphabet:
    print(f"{x} contains only alphabets.")
else:
    print(f"{x} does not contain only alphabets.")

#Task-9: Program to convert all lowercase letters in a string to uppercase manually using ASCII values.
x = input("Enter a string: ")
result = ""
for i in x:
    ascii_value = ord(i)
    if 97 <= ascii_value <= 122:
        y = ascii_value-32
        z = chr(y)
        result+=z
    else:
        result+=i
print(result)

#Task 10: Program to print all characters located at even indices of a string
s = input("Enter a string: ")
for i in range(0,len(s),2):
    print(s[i])

#Task 11: Program to count the number of words in a string
print("Number of words in a sentence checker:")
print("Please don't insert extra spaces")
x = input("Enter a sentence: ")
count = 1
for i in x:
    if i == " ":
        count += 1
print(f"The number of words is: {count}")

#Task 12: Replace all the vowels in a given word with "*".
x = input("Enter a word: ")
result = ""
x = x.lower()
for i in x:
    if i in "aeiou":
        x = x.replace(i, "*")
print(x)

#Task-13: Write a Python program to find the longest word in a given string.
x = input("Enter a string: ")
y=x.split()
longest =""
for i in y:
    if len(i)>len(longest):
        longest=i
print(longest)

#Task-14: Write a Python program to check if two strings are anagrams or not.
x = "Teacher"
y = "Cheater"
a = x.lower()
b = y.lower()
anagram = True
if len(a) != len(b):
    anagram = False
else:
    for i in a:
        if a.count(i) != b.count(i):
            anagram = False
            break
if anagram:
    print("Anagrams")
else:
    print("Not Anagrams")

#Task-15: Program to count how many special characters are present in a string.
x = input("Enter a word: ")
x = x.lower()
count = 0
for i in x:
    if '0'<=i<='9':
        pass
    elif 'a'<=i<='z':
        pass
    elif i == ' ':
        pass
    else:
        count += 1
print(f"The word contains {count} special characters")
"""

#June-5,2026
"""
#Task-1: Program to print numbers from 1 to 20 and stop when the number reaches 10 using breaks.
for i in range(1,21):
    print(i)
    if i==10:
        break

#Task-2: Program to print numbers from 1 to 15 except 8 using continue:
for i in range(1,16):
    if i==8:
        continue
    print(i)

#Task-3: Program to print numbers from 1 to 50 and stop when the first multiple of 7 greater than 20 is found.
for i in range(1,51):
    print(i)
    if i % 7 == 0 and i > 20:
        break

#Task-4: Program to print all odd numbers from 1 to 30 by skipping even numbers:
for i in range(1,31):
    if i%2==0:
        continue
    print(i)

#Task-5: Program to keep adding natural numbers starting from 1 and stop when the sum exceeds 100
sum = 0
for i in range(1,100):
    sum+=i
    print(sum)
    if sum>100:
        break    

#Task-6: Python program to print numbers from 1 to 25 except the multiples of 3.
for i in range(1,26):
    if i%3==0:
        continue
    print(i)

#Task-7: Python program to print the multiplication table of 5 and stop after 5 × 7.
for i in range(1,100):
    print(f"5x{i}={5*i}")
    if i==7:
        break

#Task-8: Python program to print numbers from 1 to 100 and stop when the first number divisible by 11 is found
for i in range(1,100):
    print(i)
    if i%11==0:
        break

#Task-9: Python program to print numbers from 1 to 20 while skipping all even numbers.
for i in range(1,21):
    if i%2==0:
        continue
    print(i)

#Task-10: Python program to print numbers from 1 to 50 and skip all numbers ending with the digit 5.
for i in range(1,51):
    if i%10==5:
        continue
    print(i)

#Task-11: Python program to find the first prime number greater than 50 and stop after finding it
for num in range(51, 100):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)
        break    

#Task-12: Python program to print numbers from 1 to 30 except those divisible by 2 or 3.
for i in range(1,31):
    if i % 3 == 0:
        continue
    if i % 2 == 0:
        continue
    print(i)

#Task-13: Python program to print the characters of a string and stop when the character 'x' is encountered.
s = input("Enter a sentence: ")
for i in s:
    if i == 'x':
        break
    print(i)

#Task-14: Python program to print all characters of a string except vowels.
s = input("Enter a sentence: ")
s = s.lower()
for i in s:
    if i in 'aeiou':
        continue
    print(i)

#Task-15: Python program to print all characters of a sentence except spaces
s = input("Enter a sentence: ")
for i in s:
    if i == ' ':
        continue
    print(i)

#Task-16: Python program to count vowels in a string and stop counting when a space is encountered.
s = input("Enter a string: ")
s = s.lower()  
vowels = 'aeiou'
count = 0
for i in s:
    if i == ' ':
        break
    if i in vowels:
        count += 1
print("Number of vowels in the string before the first space:", count)

#Task-17: Python program to print only uppercase letters from a given string.
s = input("Enter a string: ")
for i in s:
    if i.isupper():
        print(i, end="")

#Task- 18: Python program to print only lowercase letters from a given string by skipping uppercase letters
s = input("Enter a string: ")
for i in s:
    if i.isupper():
        continue
    else:
        print(i, end="")

#Task-19: Python program to read numbers from the user continuously and stop when 0 is entered.
x = int(input("Enter a number (0 to stop): "))
while True:
    if x == 0:
        print("Stopping the program.")
        break
    else:
        print(f"You entered: {x}")
        x = int(input("Enter a number (0 to stop): "))

#Task-20: Python program to allow only three password attempts and stop when the correct password is entered
correct_password = "password123"
attempts = 0
while attempts < 3:
    user_input = input("Enter the password: ")
    if user_input == correct_password:
        print("Access granted!")
        break
    else:
        attempts += 1
        print(f"Incorrect password. You have {3 - attempts} attempts left.")

#Task-21: Python program to continuously accept user input and terminate when the user enters "exit"
x = (input("Enter input (exit to stop): "))
while True:
    if x == "exit":
        print("Stopping the program.")
        break
    else:
        print(f"You entered: {x}")
        x = (input("Enter input (exit to stop): "))
"""
