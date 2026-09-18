class Solution(object):
    def climbStairs(self, n):
        n1=1
        n2=1
        for i in range(2,n+1):
            n1,n2=n2,n2+n1
        return n2