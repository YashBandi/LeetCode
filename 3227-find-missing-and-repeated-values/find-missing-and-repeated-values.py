class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total = ((n**2)*(n**2 + 1))//2
        gridSum = 0
        lookup = set()
        a = None
        for row in grid:
            for num in row:
                if num in lookup:
                    a = num
                gridSum+=num
                lookup.add(num)
        b_a = total - gridSum
        return [a,b_a + a]
        