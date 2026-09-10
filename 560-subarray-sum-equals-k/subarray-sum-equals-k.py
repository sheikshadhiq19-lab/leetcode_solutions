class Solution(object):
    def subarraySum(self, nums, k):
        p_sum=0
        h_map={0:1}
        c=0
        for i in range(len(nums)):
            p_sum += nums[i]
            if p_sum - k in h_map:
                c += h_map[p_sum - k]
            h_map[p_sum] = h_map.get(p_sum, 0) + 1
        return c