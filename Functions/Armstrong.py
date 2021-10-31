def armstrong(number):
    sums = 0
    temp = number
    d = 0
    while number != 0:
        d = number % 10
        sums += d*d*d

        number = int(number / 10)

    if sums is temp:
        return True
    else:
        return False


x = int(input("enter number :"))
ans = armstrong(x)
if ans:
    print(x, 'is Armstrong number')
else:
    print(x, 'is not Armstrong number')
