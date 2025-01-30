class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_str = t_str = 0
        while s_str < len(s) and t_str < len(t):
            if s[s_str] == t[t_str]:
                s_str += 1
            t_str += 1
        return s_str == len(s)

        
        # for i in range(len(t)):
        #     if t[i] not in s:
        #         t = t.replace(t[i]," ")
        #         i += 1
        #     else:
        #         continue
        # print(t)
        # t = t.replace(" ","")
        # print(t)
        # if t == s:
        #     return True
        # else:
        #     return False

        
        