class Solution(object):
    def removeDuplicates(self, nums):
        l1=len(nums)
        l2=len(set(nums))
        a=list(set(nums))
        n=l1-l2
        a.sort()
        while n<len(nums):
            a.append(None)
            n+=1
        nums[:]=a
        return l2