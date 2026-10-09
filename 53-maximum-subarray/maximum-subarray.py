class Solution(object):
    def maxSubArray(self, nums):
        sum1=0
        max1=nums[0]
        for i in range(0,len(nums)):
            sum1=max(nums[i],sum1+nums[i])
            max1=max(sum1,max1)
            if sum1>max1:
                max1=sum1
            if sum1<0:
                sum=0
        return max1
       