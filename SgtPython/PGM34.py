num = input("Enter a number")
if num.isdigit() == False :
    print("Ivalid number")
else:
    string_input = input('Enter a string')
    if string_input == string_input[::-1]:
        print('String is a plaindrome')
    if num == num[::-1]:
        print('Number is a plaindrome')