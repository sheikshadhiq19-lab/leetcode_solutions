class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)

        l = len(nums) - k
        i = 0
        a = []

        while l < len(nums):
            a.append(nums[l])
            l += 1

        while i < len(nums) - k:
            a.append(nums[i])
            i += 1

        nums[:] = a