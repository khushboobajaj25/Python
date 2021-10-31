integers = [int(x)for x in input("Enter integers").split()]
unique = set()
duplicate = set()
for num  in integers:
    if num in unique:
        duplicate.add(num)
    else:
        unique.add(num)

print(unique-duplicate)