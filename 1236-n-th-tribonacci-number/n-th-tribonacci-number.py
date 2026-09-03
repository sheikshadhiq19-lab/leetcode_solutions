class Solution(object):
    def tribonacci(self, n):
        l=3
        t1=0
        t2=1
        t3=1
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        while l<=n:
            s=t1+t2+t3
            t1=t2
            t2=t3
            t3=s
            l+=1
        return s
