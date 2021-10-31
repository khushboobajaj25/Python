numbers = [int(x) for x in input("Enter numbers").split()]
result = filter(lambda elem : True if elem>=3 else False,numbers)
print(result)