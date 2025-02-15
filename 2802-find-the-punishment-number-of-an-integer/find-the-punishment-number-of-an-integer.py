# class Solution:
#     def punishmentNumber(self, n: int) -> int:
#         def can_partition(s, target, index=0, current_sum=0):
#             """Recursive function to check if s can be partitioned to sum to target."""
#             if index == len(s):
#                 return current_sum == target
            
#             num = 0
#             for j in range(index, len(s)):
#                 num = num * 10 + int(s[j])  # Form number from substring
#                 if current_sum + num <= target and can_partition(s, target, j + 1, current_sum + num):
#                     return True
#             return False
        
#         punishment_sum = 0
#         for i in range(1, n + 1):  # Include n in range
#             square_str = str(i * i)
#             if can_partition(square_str, i):
#                 punishment_sum += i * i  # Add square to sum
        
#         return punishment_sum

class Solution:
    def canPartition(self, num, target):
        # Invalid partition found
        if target < 0 or num < target:
            return False

        # Valid partition found
        if num == target:
            return True

        # Recursively check all partitions for a valid partition
        return (
            self.canPartition(num // 10, target - num % 10)
            or self.canPartition(num // 100, target - num % 100)
            or self.canPartition(num // 1000, target - num % 1000)
        )

    def punishmentNumber(self, n):
        p_num = 0

        # Iterate through numbers in range [1, n]
        for curr_num in range(1, n + 1):
            sq_num = curr_num * curr_num

            # Check if valid partition can be found and add squared number if so
            if self.canPartition(sq_num, curr_num):
                p_num += sq_num

        return p_num