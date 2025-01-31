class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou" #{'a','e','i','o','u'}
        maxCount = count = sum(1 for i in s[:k] if i in vowels)
        for i in range(len(s)-k):
            if s[i] in vowels:
                count -= 1
            if s[i+k] in vowels:
                count += 1
            maxCount = max(count,maxCount)
        return maxCount


    # Solution 2: Output Limit Exceeded 98/107 Testcases. Correct code but more Runtime  
        # i = j = 0
        # n = k
        # c = 0
        # max_count = 0
        # vow = "AaEeIiOoUu"
        # for i in range(len(s)):
        #     sub_str = s[i:n]
        #     print("sub", sub_str)
        #     for j in range(len(sub_str)):
        #         if sub_str[j] in vow:
        #             c += 1
        #         j += 1
        #     i += 1
        #     n += 1
        #     max_count = max(max_count, c)
        #     c = 0
        #     if i > len(s) - k:
        #         break  
        # return max_count
                
