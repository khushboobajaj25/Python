list1 = [int(x) for x in input("Enter number").split()]
size = int(input("Enter size"))
result = []
j = 0
i =0
while i< len(list1):
    i+=size
    list2 = []
    while j<i and j<len(list1):
        list2.append(list1[j])
        j+=1
    
    result.append(list2)



print(result)

