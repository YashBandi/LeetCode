class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
         # Compute the sum of the first window
        max_sum = window_sum = sum(nums[:k])
        
        # Slide the window across the array
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]  # Add next element, remove first element of window
            # max_sum = max(max_sum, window_sum)
            if max_sum < window_sum:
                max_sum = window_sum
        return max_sum / k
        

    # Solution 2. Time Limit Exceeded 122/127 Test Cases
        # return max_sum / k
        # avg_list = []
        # i = n = 0
        # j = k
        # # while k <= len(nums):
        # for i in range(len(nums)-k+1):
        #         # s = nums[i:j]
        #     avg_list.append(sum(nums[i:j])/k)
        #     i += 1
        #     j += 1
        #     if i > len(nums) - k:
        #         break
        # return max(avg_list)    