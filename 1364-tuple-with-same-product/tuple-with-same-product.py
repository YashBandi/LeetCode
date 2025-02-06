class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = defaultdict(int)
        n = len(nums)
        count = 0

        # Step 1: Compute product pairs and store frequencies
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_map[product] += 1
        
        # Step 2: Count valid tuples
        for freq in product_map.values():
            if freq > 1:
                count += 8 * (freq * (freq - 1)) // 2  # 8 * (freq choose 2)

        return count