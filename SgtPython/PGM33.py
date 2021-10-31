a = input("Enter a number")
b = input("Enter second number")
a,b = b ,a
if(a.lstrip('-').isdigit()==False or b.lstrip('-').isdigit()==False):

    print('Invalid number')

else:
    x = int(a)
    y = int(b)


