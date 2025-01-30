class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vow = ['a','e','i','o','u','A','E','I','O','U']
        i, j = 0, len(s)-1
        while i <= j:
            if s[i] not in vow and s[j] not in vow:
                i += 1
                j -= 1
            elif s[i] not in vow:
                i += 1
            elif s[j] not in vow:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)

#Solution 2 
# Output limit exceeds for 1 test case 
        # vow = "AaEeIiOoUu"
        # x = []
        # for letter in s:
        #     if letter in vow:
        #         x.append(letter)
        # print(x)
        # ch = ""

        # for i in range(len(s)):
        #     if s[i] in vow:
        #         ch += x.pop()
        #     else:
        #         ch += s[i]
        # return ch
        



                



