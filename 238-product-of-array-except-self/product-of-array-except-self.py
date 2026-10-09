class Solution(object):
    def productExceptSelf(self, nums):
        ans=[]
        p1=1
        count=0
        for i in range(len(nums)):
            if nums[i]!=0:
               p1=p1*nums[i]
            else:
                p1=p1
                count+=1
        for i in range(len(nums)):
            if count==1 and nums[i]==0:
                ans.append(p1)
            elif count==0:
                ans.append(p1/nums[i])
            else:
                ans.append(0)
        return ans
            
            