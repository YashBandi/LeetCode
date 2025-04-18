class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = {}
        left = 0
        cnt = 0
        
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            
            while len(freq) == 3:
                cnt += len(s) - i
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
        
        return cnt
        