class Solution(object):
    def mySqrt(self, x):
        l=1
        r=x
        if x==1 or x==0:
           return x
        while l<=r:
            mid=(l+r)//2
            if mid*mid==x:
                return mid
            if mid*mid<x:
                l=mid+1
            else:
                r=mid-1
        return r