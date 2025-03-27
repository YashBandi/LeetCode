class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        split_1, split_2 = {}, {}
        for i in nums:
            split_1[i] = split_1.get(i, 0) + 1
        
        for i in range(len(nums) - 1):
            split_2[nums[i]] = split_2.get(nums[i], 0) + 1
            split_1[nums[i]] -= 1

            if split_2[nums[i]] * 2 > (i + 1) and split_1[nums[i]] * 2 > (len(nums) - i - 1):
                return i
        return -1