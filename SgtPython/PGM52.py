def based_on_extension(element):
    element.split('.')
    return element[len(element)-1]



file_names = input("Enter file names").split()
file_names.sort(key = based_on_extension)
print(file_names)