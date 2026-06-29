#June-25,2026
"""
# unordered, unindexed, doesn't allow duplicates

mySet = {10,20,30,40,50,30,60}
print(mySet)
print(type(mySet))


# add(), update() - used to merge another iterable
mySet.add(100)
print(mySet)

myList = [1,2,3]
mySet.update(myList)
print(mySet)

# remove() - used to remove one element. if the ele is not present, throw keyerror

# mySet.remove(300)
print(mySet)

# discard()- used to remove one element. if the ele is not present, doesn'tthrow keyerror

mySet.discard(20000) 
print(mySet)

# pop()

mySet.pop()
print(mySet)

# clear()
mySet.clear()
print(mySet)


# union - Returns all unique items from sets.

set1 = {1,2,3,4}
set2 = {5,6,2,7,1}
unionData = set1.union(set2)
print(unionData,"union")


# intersection() - Returns common items.
intersectionData = set1.intersection(set2)
print(intersectionData,"intersectionData")

# difference() - Returns a set containing elements present in the first set but not in the second set.

differenceData = set1.difference(set2)
print(differenceData,"difference")

# symm_diff() - Returns items in either set, but not both.

symm_diffData = set1.symmetric_difference(set2)
print(symm_diffData)


# isdisjoint - Returns True if two sets have no common elements.

a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))  # True
"""
#June-26,2026
"""
#Task-1: Given two lists, return the set of common elements that appear more than once in both lists.
def common_ele():
    a = [1, 2, 3, 4, 4, 5, 5]
    b = [4, 4, 5, 5, 6, 7, 8]
    result = []
    for x in a:
        if x in b and x not in result and a.count(x) > 1 and b.count(x) > 1:
            result.append(x)

    print(set(result))

common_ele()

#Task- 2: Create a set of unique words from a sentence, where words are separated by spaces and punctuation marks should be ignored.
sentence = input("Enter a sentence: ")
punctuation = [".", ",", "!", "?", ";", ":", "'", '"', "-", "(", ")", "[", "]", "{", "}"]
cleaned = ""
for x in sentence:
    if x not in punctuation:
        cleaned += x

words = cleaned.split()

unique_words = set()
for word in words:
    unique_words.add(word)

print(unique_words)

#Task- 3: Write a function that takes a list of numbers and returns the largest subset such that the sum of the subset is even.
def largest_even_subset(numbers):
    if not numbers:
        return []    
    total_sum = sum(numbers)
    if total_sum % 2 == 0:
        return sorted(numbers)
    odds = [x for x in numbers if x % 2 != 0]
    if not odds:
        return []
    smallest_odd = min(odds)
    result = numbers.copy()
    result.remove(smallest_odd)    
    return sorted(result)

#Task- 5: Check if two sets are equal, considering their elements but ignoring the order (i.e., set equality).
def check_set_equal():
    a = {1,2,3,4}
    b = {4,2,1,3}
    c = list(a)
    d = list(b)
    is_equal = False
    for i in range(len(c)):
        if c[i]==d[i]:
                is_equal = True
    print(is_equal)

check_set_equal()

#Task- 6:  Write a program that finds the intersection of multiple sets

def intersection_of_manysets():
    a = {1, 5, 4, 6, 3}
    b = {5, 1, 8, 4, 7}
    c = {8, 1, 5, 4, 3}
    d = {1, 4, 5, 7, 6}
   
    intersection = a.intersection(b, c, d)
    print(intersection)

intersection_of_manysets()

#Task-8: Given a list of sets, write a program to return the set containing elements that are present in every set in the list.
def elements_in_all_sets(list_of_sets):
    if not list_of_sets:
        return set()
    return set.intersection(*list_of_sets)

sets_list = [
    {1, 2, 3, 4},
    {2, 3, 5},
    {3, 6, 2}
]

common_elements = elements_in_all_sets(set_list)
print("Elements present in every set:", common_elements)

#Task-9: Write a function that checks if a set of strings forms a palindrome when concatenated together.
def check_palindrome(words):
    combined = ""
    for word in words:
        combined += word

    if combined == combined[::-1]:
        return True
    else:
        return False

words = {"mad", "am"}
result = check_palindrome(words)
print(result)

#Task-13: Write a function that checks if there exists a pair of numbers in a set that sum to a specific target.
def check_pair(numbers, target):
    for i in numbers:
        for j in numbers:
            if i + j == target and i != j:
                return True

    return False


numbers = {2, 4, 7, 9}
target = 11

result = check_pair(numbers, target)

print(result)

#Task-14: Write a function to determine whether a set is a proper subset of another set.
def check_proper_subset(set1, set2):
    if set1.issubset(set2) and set1 != set2:
        return True
    else:
        return False 

A = {1, 2}
B = {1, 2, 3}

print(check_proper_subset(A, B))

#Task-19: Count elements that appear in exactly one set
def count_unique_elements(list_of_sets):
    frequency = {}

    for s in list_of_sets:
        for i in s:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1

    count = 0

    for j in frequency:
        if frequency[j] == 1:
            count += 1

    return count


sets = [{1,2,3}, {3,4,5}, {5,6}]

print(count_unique_elements(sets))
"""