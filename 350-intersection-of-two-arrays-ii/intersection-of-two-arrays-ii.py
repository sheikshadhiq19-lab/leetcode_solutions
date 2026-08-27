class Solution(object):
    def intersect(self, nums1, nums2):
        f1={}
        a=[]
        for n in nums1:
            f1[n]=f1.get(n,0)+1
        for n in nums2:
            if f1.get(n,0)>0:
                a.append(n)
                f1[n]-=1
        return a