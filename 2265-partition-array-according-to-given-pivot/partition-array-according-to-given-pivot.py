class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, equi, more = [], [], []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equi.append(num)
            else:
                more.append(num)
        return less+equi+more
