tup = (5, 16, 23, 25, 38, 54)
print(tup.__getitem__(0))

print(tup)
print(len(tup))
seteg = {1, 2, 3, 4, 5, 5, 6}
seteg1 = {1, 2, 4, 8, }
print(seteg)
tup2 = (2, 2);
tup3 = tup.__add__(tup2)
print(tup3)
print(seteg.intersection(seteg1))
seteg1.intersection_update(seteg)
print(seteg)
print(seteg.symmetric_difference(seteg1))


