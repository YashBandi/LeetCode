class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n1 = n2 = float('inf')          #or n1 = n2 =  max(nums)
        for n in nums:
            if n <= n1:
                n1 = n     
            elif n <= n2:
                n2 = n   
            else:
                return True
        return False

       