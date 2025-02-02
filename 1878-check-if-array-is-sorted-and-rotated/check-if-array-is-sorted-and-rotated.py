class Solution:
    def check(self, nums: List[int]) -> bool:
        c = 0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                c +=1 
        if c == 1 and (nums[len(nums)-1] <= nums[0]):
            return True
        elif c == 0:
            return True
        else:
            return False
