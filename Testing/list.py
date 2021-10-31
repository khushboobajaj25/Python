nums = [10, 20, 30, 40]
print(nums)
nums.insert(2, 35)
print(nums)
del(nums[1])
print(nums)
nums.remove(40)
print(nums)
print(nums[-1])
nums = [23, 25, 38]
print(nums.append(45))
names = ["Anisha", "Khushboo", "Karan"]
mil = [nums, names]
print(mil)
# print(nums.pop(1))
del(nums[2:])
print(nums)
nums.extend([16, 5, 54])
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))
nums.sort()
print(nums)
# nums.clear()
# print(nums)
new = nums.copy()
print(new)
print(nums.count(25))
print(nums.index(54))
nums.reverse()
print(nums)
print(nums.__contains__(25))
print(nums.__getitem__(2))
nums.__delitem__(2)
print(len(nums))













