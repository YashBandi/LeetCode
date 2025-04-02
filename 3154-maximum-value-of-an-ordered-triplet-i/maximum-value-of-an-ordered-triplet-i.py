class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxval = 0
        for i in range(len(nums)):
            for k in range(len(nums) - 1, i, -1):
                j = i + 1
                while j < k:
                    maxval = max(maxval, (nums[i] - nums[j]) * nums[k])
                    j += 1
        return max(0, maxval)