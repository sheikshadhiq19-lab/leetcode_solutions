class Solution(object):
    def checkSubarraySum(self, nums, k):
        r_map={0:-1}
        p_sum=0
        for i in range(len(nums)):
            p_sum += nums[i]
            r = p_sum%k
            if r in r_map:
                p_index = r_map[r]
                if i - p_index >= 2:
                    return True
            else:
                r_map[r]=i
        return False