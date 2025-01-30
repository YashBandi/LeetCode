class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()   #['the', 'sky', 'is', 'blue']
        rev_list = x[::-1]  #['blue', 'is', 'sky', 'the']   
        return " ".join(rev_list)