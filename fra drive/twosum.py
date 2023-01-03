# https://www.youtube.com/watch?v=KLlXCFG5TnA

arr = [2,7,9,10]
target = 9

def twoSum(arr, target):
    prevMap = {} #val: index
    for i, n in enumerate(arr):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return 

print(twoSum(arr,target))
