class Solution:
    def check(self, nums: List[int]) -> bool:
        c = 0
        # nums = list(dict.fromkeys(nums))    #Removing duplicates from the nums
        #print(nums)
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                c +=1 
        #nums = list(dict.fromkeys(nums))
        print(c)
        print(nums[len(nums)-1])
        print(nums[0])
        if c == 1 and (nums[len(nums)-1] <= nums[0]):
            return True
        elif c == 0:
            return True
        else:
            return False
