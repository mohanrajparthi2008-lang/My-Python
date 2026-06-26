#June-10,2026
"""
myTuple = (10,20,30,10,40)
print(myTuple)
print(type(myTuple))

tuple1 = ("aaa",)
print(type(tuple1))

tupleConst = tuple(("aaa","aaa@gmail.com",98769456,False))
print(tupleConst)

# allow duplicates, ordered, indexed, unchangable

data = True + 10
print(data)

data1 = 2.6 + 3
print(data1)

print(myTuple[4])
print(myTuple[2:4])
print(myTuple[:3])
print(myTuple[1:])

# age, name = (10,"demo")
# print(age,name)

print(myTuple.count(10))
print(myTuple.index(30))

# for i in myTuple:
#     print(i)

convertingList = list(myTuple)
print(convertingList)

convertingTuple = tuple(convertingList)
print(convertingTuple)
"""
#June-11,2026
"""
#Task-1: Create a tuple that contains an integer, a string, and a float.
my_tuple = (-123, "user01", 12.45)
print(my_tuple)

#Task-2: Access the second element of the tuple (5, 10, 15, 20).
my_tuple = (5,10,15,20)
print(my_tuple[1])

#Task-3: Slice the tuple (1, 2, 3, 4, 5) to get the last two elements.
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[3:])

#Task-4: Concatenate the tuples (1, 2) and (3, 4).
tuple_1 = (1,2)
tuple_2 = (3,4)
print(tuple_1 + tuple_2)

#Task-5: Repeat the tuple (7, 8) three times.
my_tuple = (7,8)
print(my_tuple*3)

#Task-6: Check if 15 is present in the tuple (10, 20, 15, 25).
my_tuple = (10, 20, 15, 25)
value = 15
if value in my_tuple:
    print(value, "is found in tuple")
else:
    print("Value not found")

#Task-7: Find the length of the tuple (3, 6, 9, 12)
my_tuple = (3,6,9,12)
print("The length of the tuple is:",len(my_tuple))

#Task-8: Find the maximum and minimum values in the tuple (4, 1, 8, 3).
my_tuple = (4, 1, 8, 3)
max_value = max(my_tuple)
min_value = min(my_tuple)
print("Maximum value:", max_value)
print("Minimum value:", min_value)

#Task-9: Convert the list [1, 2, 3, 4] into a tuple.
my_list = [1,2,3,4]
my_tuple = tuple(my_list)
print(my_tuple)

#Task-10: Convert the tuple (10, 20, 30) into a list.
my_tuple = (10,20,30)
my_list = list(my_tuple)
print(my_list)

#Task-11. Find the index of the element 30 in the tuple (10, 20, 30, 40).
numbers = (10, 20, 30, 40)
value = 30
if value in numbers:
    print("The index of the given value in the tuple is:", numbers.index(value))
else:
    print("Value not found")

#Task-12: Count how many times 2 appears in the tuple (2, 3, 2, 4, 2).
my_tuple = (2,3,2,4,2)
value = 2
count = 0
for i in my_tuple:
    if i==value:
        count+=1

print(f"{value} appears {count} times in the tuple")

#Task-13: Unpack the tuple (100, 200, 300) into three separate variables.
my_tuple = (100,200,300)
a,b,c = my_tuple
print(a)
print(b)
print(c)

#Task-14: Swap the values of two tuples (1, 2) and (3, 4).
tuple_1 = (1, 2)
tuple_2 = (3, 4)
tuple_1, tuple_2 = tuple_2, tuple_1
print(tuple_1)
print(tuple_2)

#Task-15: Create a tuple that contains two other tuples (1, 2) and (3, 4).
tuple_1 = (1, 2)
tuple_2 = (3, 4)
my_tuple = (tuple_1, tuple_2)
print(my_tuple)

#Task-16: Access the number 4 from the nested tuple ((1, 2), (3, 4)).
nested = ((1, 2), (3, 4))      
print(nested[1][1])

#Task-17: Find the sum of all numbers in the tuple (5, 10, 15).
my_tuple = (5,10,15)
sum = 0
for i in my_tuple:
    sum+=i
print(sum)

#Task-18: Sort the elements of the tuple (40, 10, 30, 20) in ascending order.
my_tuple = (40,10,30,20)
my_list = list(my_tuple)
my_list.sort()
my_tuple = tuple(my_list)
print(my_tuple)

#Task-19: Reverse the elements of the tuple (1, 2, 3, 4, 5).
my_tuple = (1,2,3,4,5)
print(my_tuple[4::-1])

#Task-20: Check if all elements in the tuple (5, 5, 5, 5) are identical.
my_tuple = (5,5,5,5)
identical = True
for i in range(len(my_tuple)-1):
    if my_tuple[i]!=my_tuple[i+1]:
        identical = False
        break
if identical:
    print("All elements in the tuple is identical")
else:
    print("All elements in the tuple is not identical")
"""
