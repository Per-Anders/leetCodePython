

def maxArea(height):
    maxarea = 0
    l = 0
    r = len(height) - 1

    while l < r:
        maxarea = max(maxarea, min(height[l], height[r]) * (r-l))
        if (height[l] < height[r]):
            l += 1
        else:
            r -= 1
        return maxarea


print(maxArea([3, 2, 6, 4]))
