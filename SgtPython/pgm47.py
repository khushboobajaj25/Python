list1 = [int(x)for x in input("Enter number").split()]
n = len(list1)
unique = set()
duplicate = set()
for i in range(n):
    if list1[i] in unique:
        duplicate.add(list1[i])
    else:
        unique.add(list1[i])


print(unique)
print(duplicate)
"""
using count it takes for loop.
list1 = [int(x)for x in input("Enter number").split()]
n = len(list1)
unique = set()
duplicate = set()
for i in range(n):
    unique.add(list1[i])
    if list1.count(list1[i])>1:
        duplicate.add(list1[i])

print(unique)
print(duplicate)
"""