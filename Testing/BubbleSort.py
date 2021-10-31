n = int(input("Enter no"))
nums = list(input().split(" "))
for i in range(n):
    for j in range(n-1-i):
        if nums[j] > nums[j+1]:
            nums[i], nums[j]=nums[j], nums[i];
print(nums)
