lst = [x for x in input("Enter string").split()]
result = map(lambda  x: x.lower(),lst)
for x in result:
    print(x)