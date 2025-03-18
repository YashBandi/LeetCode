class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        hs = defaultdict(int)
        ans = 0
        while r < len(nums):
            tmp = bin(nums[r]).replace("0b", "")
            flag = True
            for i, j in zip(range(len(tmp)),tmp[::-1]):
                if int(j) == 1: hs[i] += int(j)
                if hs[i] >= 2:
                    flag = False
            
            while flag == False:
                flag = True
                tmp = bin(nums[l]).replace("0b", "")
                for i, j in zip(range(len(tmp)),tmp[::-1]):
                    hs[i] -= int(j)

                for i in hs:
                    if hs[i] >= 2:
                        flag = False
                l += 1

            ans = max(ans, r - l + 1)

            # print(hs, ans)
            r += 1

        return ans