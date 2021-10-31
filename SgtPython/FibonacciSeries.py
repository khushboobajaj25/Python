n = int(input("Enter number"))
f = 0
s = 1
print(f, s,end=" ")

t = 0
for i in range(n):
    t = f+s
    f = s
    s = t
    print(t,  end=" ")
