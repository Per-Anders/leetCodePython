
class Solution:
    def moveZeros(self, nums):
        j = 0
        n = len(nums)
        for num in nums:
            if (num !=0):
                nums[j] = num
                j+=1
        for x in range(j,n):
            nums[x] = 0

        return nums

    def moveZeros(self, nums):
        j =0
        n = len(nums)
        for num in nums:
            if(num != 0):
                nums[j] = num 
                j+=1
        for x in range(j,n):
            nums[x] = 0
        return nums

s = Solution()
print(s.moveZeros([0,1,0,3,12]))