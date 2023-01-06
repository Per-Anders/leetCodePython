# https://www.youtube.com/watch?v=73r3KWiEvyk


nums = [1,3,5,1]

def rob(nums):
    rob1, rob2 = 0,0

    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2 

print(rob(nums))

