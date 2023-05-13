# take in a list of numbers and turn that numbers into its corresponding int, input [2,1] returns twenty one

nums = [1,2,3,4,5,6]
numSum = 0

for i,num in enumerate(nums):
    numSum += num * 10 ** i # nums = nums + num to the current power of 10 (element would be multiplied by 1)

print(numSum)

##################################################################################################################################
# the below code will return the int in non-reverse order 
nums = [1,2,3,4,5,6]
numSum = 0
count = len(nums) - 1

for i,num in enumerate(nums):
    numSum += num * 10 ** count # nums = nums + num to the current power of 10 (element would be multiplied by 1)
    count -= 1

print(numSum)






