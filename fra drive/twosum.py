# https://www.youtube.com/watch?v=KLlXCFG5TnA

arr = [2,7,9,10]
target = 9

def twoSum(arr, target):
    prevMap = {} #val: index 
    # {}
    for i, n in enumerate(arr): 
        # Første iterasjon
        # i = 0
        # n = 2
        # Andre iterasjon
        # i = 1
        # n = 7
        diff = target - n
        #Første iterasjon
        # 7 = 9 - 2
        # Andre iterajson
        # 2 = 9 - 7
        if diff in prevMap:
            #hvis 7 er i hashmap returnner val: index
            #hvis 2 er i hashmap returner val: index
            return [prevMap[diff], i]
            # 2 er i hashmap, returner index til 2=0, og i=1, [0,1]
        prevMap[n] = i
        # {2: 0}
    return 







