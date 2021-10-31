# wap to sort integers in a list in desc order wothout using reverse keyword
def descending(number):
    return -number
list1= [ int(x) for x in input("Enter numbers").split()]
list1.sort(key = descending)
print(list1)