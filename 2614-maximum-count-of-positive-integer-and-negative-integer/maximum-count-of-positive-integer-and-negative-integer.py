class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        idx = bisect_left(nums,0)
        idx1 = bisect_left(nums,1)
        return max(idx,n-idx-(idx1-idx))
        