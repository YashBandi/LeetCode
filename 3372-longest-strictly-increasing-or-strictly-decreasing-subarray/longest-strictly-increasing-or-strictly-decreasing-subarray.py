class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        c1 = c2 = 1
        max_length = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                c1 += 1
                c2 = 1       
            elif nums[i] > nums[i+1]:
                c1 = 1
                c2 += 1    
            else:
                c1 = c2 = 1 
            max_length = max(max_length, c1, c2)       
        return max_length

       