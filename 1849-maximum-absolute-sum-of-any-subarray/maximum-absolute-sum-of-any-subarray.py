class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        presum = [0]
        for i in range(len(nums)): 
            presum.append(presum[-1] + nums[i])
            
        return max(presum) - min(presum)
        
        