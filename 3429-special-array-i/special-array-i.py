class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        temp = []
        if len(nums) < 2:
            return True
        for i in range(1,len(nums)):
            if (nums[i-1]%2 == 0 and nums[i]%2 != 0) or (nums[i-1]%2 != 0 and nums[i]%2 == 0):
                temp.append(1)
            else:
                temp.append(0)
            # i += 1
        res = all(temp)
        return res

        