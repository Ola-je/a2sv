class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack =[]
        for i in s:
            if i =='(':
                stack.append(i)
            elif i ==')' and stack and stack[-1]=='(':
                stack.pop()
            elif i ==')' and stack and stack[-1]!='(':
                stack.append(i)
            elif i==')' and not stack:
                stack.append(i)
        return len(stack)