numbers = [int(x) for x in input("Enter numbers").split()]
squares = map(lambda elem: elem**2,numbers)
print(squares)