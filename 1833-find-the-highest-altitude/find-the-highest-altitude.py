class Solution(object):
    def largestAltitude(self, gain):
        p_sum=0
        a=[0]
        for i in range(len(gain)):
            p_sum+=gain[i]
            a.append(p_sum)
        return max(a)