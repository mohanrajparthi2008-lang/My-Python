#June-4,2026:
"""
#Task-16: Program to print each character of a string a given number of times:
print("Print each character of a string given number of times:")
s = input("Enter a word: ")
count = int(input("How many times should characters be repeated: "))
for i in s:
    print(i * count)

#Task-17: Program to remove duplicate characters from a string:
print("Remove Duplicate Characters")
x = input("Enter a word: ")
x = x.upper()
result = ""
for i in x:
    if i not in result:
        result += i
print(result)

#Task-18: Program to count the number of consonants in a given string.
print("Number of consonants in a string checker: ")
x = input("Enter a word: ")
count = 0
x = x.lower()
for i in x:
    if 'a' <= i <= 'z' and i not in "aeiou":
        count+=1
print(f'The number of consonants is: {count}')

#Task-19: Program to capitalize the first letter of a string manually (without using capitalize())
print("Capitalize function")
x = input("Enter a string: ")
x = x.lower()
if x.isalpha():
    y = x[0]
    z = ord(y)
    a = chr(z-32)
    b = x[1:]
    print(a+b)
else:
    print(x)

#Task-20: Program to print characters of a string until a vowel is encountered
print("Print character until a vowel is encountered")
x = input("Enter a word: ")
x = x.lower()
output =""
for i in x:
    if i in "aeiou":
        break
    output+=i
print(output)
"""
