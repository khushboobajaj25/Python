
def convert(number,list1):
    if number>0:
        list1.append(number%2)
        convert(number/2,list1)

number = int(input("Enter decimal number"))
list1 =[]
convert(number ,list1)
print(list1.reverse())
