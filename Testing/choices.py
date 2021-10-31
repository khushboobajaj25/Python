def print_diamond(number,character,letter):
    num = number-2
    charcter_count =0
    while num != -2:
        print(character*charcter_count,end="")
        print("\\", end="")
        print(letter*num,end="")
        print("/")
        num -= 2
        charcter_count += 1
    num=0
    charcter_count-=1
    while num != number:
        print(character*charcter_count,end="")
        print("/",end="")
        print(letter*num,end="")
        print("\\")
        num+=2
        charcter_count-=1


print("0. Exit")
print("1.Print a diamond")
print("2.Print a Number Pattern")
print("3.Print a cost table ")
option = int(input("Enter your option: "))
if option == 0:
    print()
elif option == 1:
    length = -1
    while (length % 2 != 0 or (not (length >=0 or length <=20))):
        length = int(input("Enter even length whose lenegth between 0 to 20"))

    print_diamond(length, '*', 'T')
elif option == 2:
    pass

else:
    pass