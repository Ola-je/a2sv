class Solution:
    def maxScore(self, s: str) -> int:
        sum1 = sum(map(int, s))
        sum0 = 0
        max_ = float('-inf')

        for i in range(len(s)-1):
            if int(s[i]) == 1:
                sum1 -=1
            else:
                sum0 +=1
            max_ = max(max_, sum1+sum0)
        return max_
