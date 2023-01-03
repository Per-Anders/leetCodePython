# https://www.youtube.com/watch?v=3OamzN90kPg

nums = [1,2,1,3,4,5]

def containsDuplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False 


print(containsDuplicate(nums))

