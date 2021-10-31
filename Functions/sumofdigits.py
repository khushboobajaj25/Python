def sum_of_first_n(number):
    if number == 0:
        return 0
    else:
        return number + sum_of_first_n(number-1)


x = int(input("Enter positive number"))
y = sum_of_first_n(x)
print(y)
