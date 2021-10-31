#wap to take list of integers as an input and output cumulative addition on that [2,6,5] o/p [2,8,13]
list1 = [int(x)for x in input("Enter number").split()]
n = len(list1)
for i in range(n):
    if i == 0:
        pass
    else:
        list1[i] = list1[i]+list1[i-1]
print(list1)
