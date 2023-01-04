# https://www.youtube.com/watch?v=Y0lT9Fck7qI

#dynamic programming

n = 5

def climbStairs(n):
    one, two = 1,1

    for i in range(n-1):
        temp = one
        one = one + two
        two = temp
    return one 

print(climbStairs(n))