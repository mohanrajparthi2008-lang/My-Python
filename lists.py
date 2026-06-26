#June-8,2025: Class
"""
myList = [10,20,30,40,50,20,50]

print(myList)

# used to store multiple elements in a single variable
studentData = ["St001","demo","demo@gmail.com",4983578476, True, 5.5]
print(studentData,"studentData")
# list constructor
listWithCons = list((1,2,3))
print(listWithCons,"listWithCons")



# changable, allow duplicates, ordered, indexed


# accessing the list

print(myList[3])
print(myList[1:3])
print(myList[:2])
print(myList[2:])

myList[1] = 200
print(myList,"after change")


# append - used to add element in the last index
myList.append(350)
print(myList,"after append")

# insert() - used to add ele in specific index

myList.insert(4,12)
print(myList,"after insert()")

#pop() - used to remove ele
myList.pop()
print(myList,"pop()")

myList.pop(2)
print(myList,"pop()")


# remove(element): Removes the first occurrence of a specific value from the list.

myList.remove(50)
print(myList,"remove()")

# extend(iterable): Adds all elements from another iterable (like a list or tuple) to the end.


myList.extend(listWithCons)
print(myList,"extend")

# clear(): Removes every single item from the list, leaving it completely empty

# myList.clear()
# print(myList,"clear()")


# count()

countData = myList.count(200)
print(countData,"count()")

#Returns the index position of the first occurrence of a specific value
specificIndex = myList.index(12)
print(specificIndex,"index()")

# myList.sort()
print(myList)

myList.reverse()
print(myList)
"""

#June-9,2026
"""
print("Task-1: Python program to print all elements of a list using a loop.")
list = [45,63,21,15,89,15,12]
for i in list:
    print(i)

print("Task-2: Python program to print only the even numbers from a list")
list = [45,63,21,15,89,15,12]
for i in list:
    if i%2==0:
        print(i)
    else:
        continue

print("Task-3: Python program to print only the odd numbers from a list.")
list = [45,63,21,15,89,15,12]
for i in list:
    if i%2!=0:
        print(i)
    else:
        continue

print("Task-4: Python program to find the sum of all numbers in a list")
list = [45,63,21,15,89,15,12]
sum = 0
for i in list:
    sum+=i
print(sum)

print("Task-5: Program to find the largest number in a list using loop")
list = [41,22,89,16,12]
largest = list[0]
for i in list:
    if i>largest:
        largest=i
print("The largest number in the list is",largest)

print("Task-6: Program to find the smallest number in a list using loop")
list = [41,22,89,16,12]
smallest = list[0]
for i in list:
    if i<smallest:
        smallest=i
print("The smallest number in the list is",smallest)

print("Task-7: Python program to count how many positive numbers are in a list")
list = [45,63,-21,15,-89,15,-12]
count_positive = 0
for i in list:
    if i>0:
        count_positive+=1
    else:
        continue
print(count_positive)

print("Task-8: Python program to ccount how many negative numbers are in a list")
list = [45,63,-21,15,-89,15,-12]
count_negative = 0
for i in list:
    if i<0:
        count_negative+=1
    else:
        continue
print(count_negative)

print("Task-9: Python program to reverse a list without using the .reverse() method.")
number = [3,9,11,6]
reverse = []
for i in range(len(number)-1,-1,-1):
    reverse.append(number[i])
print(reverse)

print("Task-10: Program to count how many even and odd numbers are present in a list")
list = [41,22,89,16,12]
count_odd = 0
count_even = 0
for i in list:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print("The number of odd numbers in the list is:",count_odd)
print("The number of even numbers in the list is:",count_even)

print("Task-11: Program to find and print the index of a specific value in a list")
numbers = [41,22,89,16,12]
value = int(input("Enter the value of element: "))
for i in range(len(numbers)):
    if numbers[i]==value:
        print("The index of the given value in the list is:",i)
        break
else:
    print("Value not found")

print("Task-12: Program to replace all negative numbers in a list with 0).")
numbers = [-12, 25, -18, -75, -50, 90, 30]
for i in range(len(numbers)):
    if numbers[i]<0:
        numbers[i]=0    
print(numbers)
    
print("Task-13: Python program to print all numbers greater than 50 from a list")
list = [45,63,21,15,89,15,12]
for i in list:
    if i>50:
        print(i)

print("Task-14: Program to create a new list containing the squares of each element")
numbers = [3,9,11,6]
new_list = []
for i in range(len(numbers)):
    square=numbers[i]*numbers[i]
    new_list.append(square)
print(new_list)        

print("Task-15: Python program to print all duplicate values in a list.")
numbers = [41, 16, 12, 16, 12]
seen = []
duplicates = []
for num in numbers:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    else:
        seen.append(num)
print(duplicates)

print("Task-16: Program to print list elements until the number 50 appears (stop when found).")
numbers = [12, 25, 18, 75, 50, 90, 30]
for i in numbers:
    if i==50:
        break
    else:
        print(i)

print("Task-17: Program to count how many numbers in a list are divisible by 5")
list = [45,63,21,15,89,15,12]
div_5=0
for i in list:
    if i%5==0:
        div_5+=1
print(f"Numbers in the list which is divisible by 5: {div_5}")

print("Task-18: Python program to find the second largest number in a list.")
number = [3, 9, 11, 6]
number.sort()
second_largest = number[len(number)-2]
print(second_largest)

print("Task-19: Python program to check whether a list is sorted in ascending order.")
number = [3, 9, 11, 6]
is_sorted = True
for i in range(len(number) - 1):
    if number[i] > number[i + 1]:
        is_sorted = False
        break
    
if is_sorted:
    print("Sorted in ascending order")
else:
    print("Not sorted")

print("Task-20: Program to sum of only the even numbers in a list.")
list = [41,22,89,16,12]
sum_even = 0
for i in list:
    if i%2==0:
        sum_even+=i
print(f"The sum of even numbers in the list is {sum_even}")
"""
