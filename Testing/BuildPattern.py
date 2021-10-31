def build_pattern_asc(num1,num2):
    n = num2-num1+1
    for i in range(0,n):
        print("      "*i,end="")
        row_percentage = num1*0.1
        "{0:.2f}".format(row_percentage)
        coloumn_integer = num1
        for j in range(coloumn_integer,num2+1):
            print("{0:.2f}".format(row_percentage*j)," ",end="")

        print()
        num1+=1

def build_pattern_desc(num1,num2):
    n = num2-num1+1
    num = num2
    for i in range(n,0,-1):
        print("      "*i,end="")
        row_percentage = num2*0.1
        "{0:.2f}".format(row_percentage)
        coloumn_integer = num2
        for j in range(coloumn_integer,num+1):
            print("{0:.2f}".format(row_percentage*j)," ",end="")

        print()
        num2-=1

#build_pattern_asc (3, 9)
build_pattern_desc(3, 9)
