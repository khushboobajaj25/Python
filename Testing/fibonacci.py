x = int(input("Enter a number"))
f = 0
s = 1
t = 0
print(f)
print(s)

for i in range(10, 1, 1):
    t = f+s
    print(t)
    f = s
    s = t
    i = i+1
