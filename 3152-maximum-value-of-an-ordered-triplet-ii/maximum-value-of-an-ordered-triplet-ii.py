class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        x = 0
        dif = 0
        max_val = 0

        for n in nums:
            max_val = max(max_val, dif * n)
            dif = max(dif, x - n)
            x = max(x, n)
        return max_val