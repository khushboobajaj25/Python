s1 = set(input("Enter a set1").split())
s2 = set(input("Enter a set2").split())
if(s1.issuperset(s2) and len(s1)>len(s2)):
    print("Yes")
else:
    print("No")
