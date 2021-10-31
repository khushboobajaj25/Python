def based_on_length(element):
    print('func called with param and i am returning len of element')
    return len(element)
integers = [3,4,25,18,23,38]
integers.sort()
print(integers)
words=["life","is","beautiful","if","you","are"]
words.sort()
print(words)
# custom sort not natural sort
# sort the words list based on their length
words.sort(key =based_on_length)
print(words)