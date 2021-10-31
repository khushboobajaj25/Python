n = int(input("Enter no of lines"))
l = []

x = n+1
y = -1
for i in range(n):
    x -= 1
    #print(x)
    l2 =[]
    y+=1
    #for j in range(x):
        #print(" ", end="")

    if y == 0:

        l2 = [1]
        l.append(l2)
    elif y == 1:

        l2 = [1,1]
        l.append(l2)
    else:

        l3 = l[len(l)-1]
        l2.append(1)
        length = len(l3)-1
        for i in range(length):
            l2.append(int(l3[i])+int(l3[i+1]))
        l2.append(1)
        l.append(l2)


print(*l,sep ="\n")


