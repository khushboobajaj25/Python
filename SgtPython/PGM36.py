string_input = input("Enter string")
print(sorted(string_input))
sorted_list =  sorted(string_input,reverse=True)
sorted_string = "".join(sorted_list)
print(sorted_string)