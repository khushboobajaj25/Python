a = int(input("Enter initial range"))
b = int(input("Enter final range"))
for i in range(a, b, 1):
    if i % 2 == 0:
        print(i, end=" ")

"""

even_numbers = range(a,b,2)
for nums in even_numbers:
    print(list(even_numbers))

"""
a = a+1 if a % 2 == 1 else 0
