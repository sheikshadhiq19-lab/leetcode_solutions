class Solution(object):
    def frequencySort(self, s):
        f={}
        a=[]
        for i in s:
            f[i]=f.get(i,0)+1
        r=""
        for i in sorted(f, key=f.get, reverse=True):
            r += i * f[i]
        return r
        