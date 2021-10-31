lst = input("Enter strings").split()
anagrams = {}
for i in lst:
    key = "".join(sorted(i))
    print(key)
    temp = anagrams.get(key)
    if temp is None:
        anagrams[key] = [i]
    else:
        anagrams[key].append(i)


[print(x) for x in anagrams.values() if len(x)>1]