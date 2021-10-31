n = int(input("Enter a no of rows"))
x = n+1
for i in range(n):
    x -= 1
    for j in range(x):
        print(" ",end="")
    for k in range(i+1):
        print("* ",end="")
    print()