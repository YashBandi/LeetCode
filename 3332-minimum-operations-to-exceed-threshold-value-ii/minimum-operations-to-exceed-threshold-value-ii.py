class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        val = 0

        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            val += 1

        return val

        # Solution 2
        # ans = 0
        # arr = SortedList(nums)
        # while len(arr) > 1 and k > arr[0]:
        #     ans += 1
        #     arr.add((arr[0] * 2) + arr[1])
        #     arr.discard(arr[1])
        #     arr.discard(arr[0])
        # return ans
        