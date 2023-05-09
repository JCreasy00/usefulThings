nums = [1,2,3,4,5,6]
numSum = 0

for i,num in enumerate(nums):
    numSum += num * 10 ** i # nums = nums + num to the current power of 10 (element would be multiplied by 1)

print(numSum)






