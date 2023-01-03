# https://www.youtube.com/watch?v=5Km3utixwZs

n = 1001

# def hammingWeight(n):
#     res = 0
#     while n:
#         res += n % 2
#         n = n >> 1
#     return res 


# print(hammingWeight(n))

def hammingWeight(n):
    res = 0
    while n:
        n &= (n -1 )
        res += 1
    return res 

print(hammingWeight(n))
