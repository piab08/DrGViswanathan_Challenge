class Solution:
    def majorityElement(self, nums):
        d = {}

        for i in nums:
            d[i] = d.get(i, 0) + 1

            if d[i] > len(nums) // 2:
                return i