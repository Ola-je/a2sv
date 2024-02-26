class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        length = 0
        for i, k in enumerate(s):
            if k == '(':
                length +=1
            else:
                length -=1
                if s[i-1] == '(':
                    ans += 2**length
        return ans