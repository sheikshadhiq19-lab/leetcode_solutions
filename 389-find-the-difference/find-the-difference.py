class Solution(object):
    def findTheDifference(self, s, t):
        l1=list(s)
        l2=list(t)
        for i in range(len(l1)):
            if l1[i] in l2:
                l2.remove(l1[i])
        return "".join(l2)
        