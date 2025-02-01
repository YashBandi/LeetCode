class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        for i in range(1,len(nums)):
            if nums[i-1]%2 == nums[i]%2:    #Just checking no 2 adjacent elements are both even or both odd. If both are even then % gives 0, if both odd % gives 1. So, return false if 0 == 0 or 1 == 1.
                return False
        return True