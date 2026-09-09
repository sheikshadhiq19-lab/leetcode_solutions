class Solution(object):
    def numberOfPoints(self, nums):
        ans=[]
        for i in range(len(nums)):
            a=nums[i][0]
            while a<=nums[i][1]:
                ans.append(a)
                a=a+1
        return len(set(ans))