class Solution(object):
    def maxProfit(self, prices):
        min_p=prices[0]
        max_p=float('-inf')
        for i in range(len(prices)):
            min_p=min(prices[i],min_p)
            max_p=max(max_p,prices[i]-min_p)
        return max_p
          