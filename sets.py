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