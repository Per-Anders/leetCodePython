# https://www.youtube.com/watch?v=5WZl3MMT0Eg

nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
    maxSub = nums[0]
    curSum = 0

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n 
        maxSub = max(maxSub, curSum)
    return maxSub


print(maxSubArray(nums))
