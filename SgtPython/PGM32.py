main_string = input("Enter string")
sub_string = input("ENter string")
print(main_string.count(sub_string))
pos = 0
start = 0
count = 0
while pos !=-1:
    pos = main_string.find(sub_string,start)
    if(pos!=-1):
        count+=1
    start=pos+len(sub_string)
print(count)

