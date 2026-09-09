class Solution(object):
    def pivotIndex(self, nums):
        s=sum(nums)
        l=0
        for i in range(len(nums)):
            r=s-l-nums[i]
            if l==r:
                return i
            l=l+nums[i]
        return -1