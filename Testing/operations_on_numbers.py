x = int(input("Enter 1st positive number"))
temp = x
sum = 0
product =1
reverse = 0
while temp != 0:
    d = int( temp % 10)
    sum += d
    product *= d
    reverse = reverse*10+d
    temp = int(temp/10)
print(f'sum of digits {sum}')
print("product of dits is", product)




