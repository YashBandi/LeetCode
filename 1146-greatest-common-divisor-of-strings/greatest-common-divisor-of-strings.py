class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if str1+str2 = str2+str1 then both strings share the same repeating pattern, else there's no common divisor. So we're returning an empty string
        if str1 + str2 != str2 + str1:
            return ""
        # consider ex.2 gcd(6,4) is 2. So our substring of length 2 is repeating. And as per the hint, the prefixes are same. So, return either str1[:2] or str2[:2]
        return str1[:gcd(len(str1),len(str2))]
        