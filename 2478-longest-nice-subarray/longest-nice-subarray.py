class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        maxlen = 0
        bitwiseOR = 0

        for right in range(len(nums)):
            while bitwiseOR & nums[right] != 0:
                bitwiseOR ^= nums[left]
                left += 1
            
            bitwiseOR |= nums[right]
            maxlen = max(maxlen, right - left +1)
        
        return maxlen