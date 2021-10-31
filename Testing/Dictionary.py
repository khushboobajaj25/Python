"""data ={1: 'Karan', 2: 'Khushboo', 3: 'Anisha'}
print(data)
print(data[1])
print(data[2])
print(data[3])
print(data.get(4))
print(data.get(4, 'Not Found'))
language = ['Python', 'Java', 'CSharp']
rating = ['Good', 'Best', 'Better']
lang = dict(zip(language, rating))
print(lang)
data['Pagal'] = 'Sabh'
print(data)
prog = {'JS': 'Atom', 'CS': 'VS', 'Phython': ['Pycharm', 'Sublime'], 'Java': {'JSE': ['Netbeans'], 'JEE': ['Eclipse']}}
print(prog)
"""
rollnos=[1,2,3,4,5]
name=['ABC','XYZ','LMN','QRS','UVW']
dict={k:v for k,v in zip(rollnos,name)}
print("Dictionary on mapping", dict)
# i) Update
dict.update({3: 'DEF'})
print("Dictionary on update", dict)
# ii) concatenate
dict.update({6: 'KIT',7:'HIJ'})
print("Dictionary on concatenation", dict)
# iii) delete
del dict[6]
print("Dictionary on deleting", dict)
# iV) Search a key
no=int(input("Enter the roll no to be seacrched:"))
if no in dict.keys():
    print("Key found ",no,dict[no])
else:
    print("Key not found",no)
