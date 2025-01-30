class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mer = ""
        n1 = len(word1)
        n2 = len(word2)
        if n1==n2:
            for i in range(n1):
                mer = mer + word1[i]+word2[i]
        if n1>n2:
            for i in range(n2):
                mer = mer + word1[i]+word2[i]
            mer = mer + word1[n2:n1+1]
        if n1<n2:
            for i in range(n1):
                mer = mer + word1[i]+word2[i]
            mer = mer + word2[n1:n2+1]
        return mer
            



