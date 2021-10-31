n = int(input("Enter number"))
triplets =[]
for i in range (n):
    for j in range(i,n):
        if(i+j<n):
            triplets.append([i,j,i+j])
        else:
            break

print(triplets)
list1 = [[i,j,i+j] for i in range(1,n) for j in range(i,n) if i+j<n]
print(list1)