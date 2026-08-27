class Solution(object):
    def topKFrequent(self, nums, k):
        f={}
        a=[]
        for n in nums:
            f[n]=f.get(n,0)+1
        return sorted(f, key=f.get, reverse=True)[:k]