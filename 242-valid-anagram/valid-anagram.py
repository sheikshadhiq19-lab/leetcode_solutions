class Solution(object):
    def isAnagram(self, s, t):
        f={}
        if len(s)==len(t):
            for i in s:
                f[i]=f.get(i,0)+1
            for i in t:
                if f.get(i,0)>0:
                    f[i]-=1
                else:
                    return False
        else:
            return False
        return True

        