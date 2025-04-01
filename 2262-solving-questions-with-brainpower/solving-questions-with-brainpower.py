class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def check(i: int) -> int:
            return 0 if i >= len(questions) else max(check(i + 1), questions[i][0] + check(i + 1 + questions[i][1]))
        return check(0)