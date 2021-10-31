x = input("Enter a number")
n = len(x)
sum = 0
number = int(x)
temp = int(x)
while number != 0:
    d = number % 10
    sum += d**n
    number = int(number/10)
if sum == temp:
    print(temp, "is armstrong number")
else:
    print(temp, "is not armstrong number")
