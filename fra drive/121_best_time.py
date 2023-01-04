# https://www.youtube.com/watch?v=1pkOgXD63yU

# two pointers

prices = [7,2,5,6]

def maxProfit(prices):
    l, r = 0, 1 # left = buying, right is selling
    maxP = 0

    while r < len(prices):
        #profitable?
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r+= 1
    return maxP


# print(maxProfit(prices))


