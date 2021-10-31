initial = int(input("Enter initial range"))
final = int(input("Enter final range"))
if initial == 1:
    initial += 1
for i in range(initial,final+1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i)