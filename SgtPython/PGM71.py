name_age = dict(x.split()for x in input("Enter name and age of person").split(","))
#Largest_name = sorted(name_age.items() ,key =len )
Largest_name = max(name_age.keys(),key=len)
#print(Largest_name[len(Largest_name)-1])
print(Largest_name)
#Largest_age = sorted(name_age.items() ,key =lambda name_age:int(name_age[1] ))
Largest_age= min(name_age.items() ,key =lambda name_age:int(name_age[1] ))
#print(Largest_age[len(Largest_age)-1])
print(Largest_age)
"""
Modification:
max(
min
"""