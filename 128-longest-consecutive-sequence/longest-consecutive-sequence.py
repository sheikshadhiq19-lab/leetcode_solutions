class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        s=set(nums)
        l=0
        for n in s:
            if n-1 not in s:
                current=n
                c=1
                while current+1 in s:
                    current+=1
                    c+=1
                l=max(l,c)
        return l