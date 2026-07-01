#June-30,2026: Built in Functions:
"""
from functools import reduce
#Task-1: Use `reduce()` to find the **sum** of all elements in a list of integers.
integers = [1,2,-3,0,4,11,-5]
result = reduce(lambda x,y: x+y, integers)
print(result)

from functools import reduce
#Task-2: Use `reduce()` to find the **product** of all elements in a list of integers.
integers = [1,2,-3,4,11,-5]
result = reduce(lambda x,y: x*y, integers)
print(result)

from functools import reduce
#Task-3: Use `reduce()` to find the **largest element** in a list.
numbers = [1,23,4,5]
largest_element = reduce(lambda x, y: x if x > y else y, numbers)
print(largest_element)

from functools import reduce
#Task-4: Use `reduce()` to **concatenate** all strings in a list into a single string.
words = ['I',' ', 'love',' ', 'programming']
result = reduce(lambda x,y: x+y, words)
print(result)

from functools import reduce
#Task-5: Use `reduce()` to find the **total number of characters** in a list of strings.
words = ['apple', 'banana', 'cherry']
total_characters = reduce(lambda count, x: count + len(x), words, 0)
print(total_characters)

#Task-6: Write a program to filter all even numbers from a list.   
numbers = [1,2,3,4,5,6,7,8]
result = list(filter(lambda x: x%2==0, numbers))
print(result)

#Task-7: Filter all odd numbers from a list.
numbers = [1,2,3,4,5,6,7,8]
result = list(filter(lambda x: x%2!=0, numbers))
print(result)

#Task-8: Filter all positive numbers from a list.
numbers = [1,2,-3,4,-5,6,7,-8]
result = list(filter(lambda x: x>0, numbers))
print(result)

#Task-9: Filter all negative numbers from a list.
numbers = [1,2,-3,4,-5,6,7,-8]
result = list(filter(lambda x: x<0, numbers))
print(result)

#Task-10: Filter all numbers greater than 50
numbers = [10,20,-30,40,-50,60,70,-80]
result = list(filter(lambda x: x>50, numbers))
print(result)

#Task-11: Use map() to double each number in the list [1, 2, 3, 4, 5].
my_list = [1, 2, 3, 4, 5]
double = list(map(lambda x: x*2, my_list))
print(double)

#Task-12: Use map() to convert the list ["1", "2", "3", "4"] into integers.
string_list = ["1", "2", "3", "4"]
int_list = list(map(int, string_list))
print(int_list)

#Task-13: Use map() to convert the list ["apple", "banana", "mango"] into uppercase letters.
fruits = ["apple","banana","mango"]
upper = list(map(str.upper, fruits))
print(upper)

#Task-14: Use map() to find the length of each word in the list ["cat", "dog", "fish"].
words = ["cat", "dog", "fish"]
lengths = list(map(len, words))
print(lengths)

#Task-15: Use map() to add 10 to each number in the list [5, 10, 15, 20].
numbers = [5, 10, 15, 20]
result = list(map(lambda x: x + 10, numbers))
print(result)

#Task-16. Use map() to triple each number in a list of integers.
numbers = [5, 10, 15, 20]
result = list(map(lambda x: x * 3, numbers))
print(result)

#Task-17. Use map() to convert all strings to lowercase in a list of words.
words = ["APPLE", "BANANA", "MANGO"]
lower = list(map(str.lower, words))
print(lower)

#Task-18. Use reduce() to find the minimum element in a list of integers.
numbers = [5, 2, 9, 1, 7]
from functools import reduce
minimum = reduce(lambda x, y: x if x < y else y, numbers)
print("The minimum element in the list is:", minimum)

#Task-19. Use reduce() to join all words with spaces into one sentence.
from functools import reduce
words = ["I", "love", "programming"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)

#Task-20. Filter all numbers that are multiples of 3 from a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiples_of_3 = list(filter(lambda x: x % 3 == 0, numbers))
print(multiples_of_3)

#Task-21. Filter all strings that start with a vowel from a list of words.
words = ["apple", "banana", "orange", "grape", "kiwi", "avocado", "pear"]
words = list(map(str.lower, words))
vowel_words = list(filter(lambda x: x[0] in 'aeiou', words))
print(vowel_words)
"""