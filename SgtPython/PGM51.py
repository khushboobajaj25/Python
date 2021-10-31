def square (numbers):
    for i in range(len(numbers)):
        numbers[i]=numbers[i]**2

list1 = [int(x) for x in input("Enter number").split()]
square(list1)
print(list1)
list1 = [int(x**2) for x in input("Enter number").split()]