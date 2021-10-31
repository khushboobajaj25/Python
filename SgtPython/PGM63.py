n = int(input("Enter number n "))
numbers ={}
for i in range(0,n):
    numbers[i]=i**2

print(numbers)
numbers = dict((i,i**2) for i in range(0,n))
print(numbers)
