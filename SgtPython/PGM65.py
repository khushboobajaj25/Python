import collections
"""strings = input("Enter strings")
string_count ={}
for word in strings:
    if word in string_count:
        string_count[word]=string_count[word]+1
    else:
        string_count[word] = 1

print(string_count)
"""
string_count  = collections.Counter([1,1,1,2,3,4,5,6])
print(dict(string_count))