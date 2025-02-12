class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Get the sum of all elements in nums
        left_sum = 0  # Initialize left sum as 0
        
        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]  # Compute right sum dynamically
            
            if left_sum == right_sum:  # Check pivot condition
                return i  # Return the first pivot index
            
            left_sum += nums[i]  # Update left sum
        
        return -1  # Return -1 if no pivot index is found