numbers = [int(x) for x in input("Enter numbers").split()]
odd = list(filter(lambda num: num%2==1,numbers))
even = filter(lambda num: num%2==0,numbers)
print(odd)
print(even)