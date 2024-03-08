class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {'+': lambda first, second: first+second, 
                    '-': lambda first, second: first-second,
                    '*': lambda first, second: first*second,
                    '/': lambda first, second: int(first/second)}
        for i in tokens:
            if i in operands:
                second = stack.pop()
                first = stack.pop()
                stack.append(operands[i](first,second))
            else:
                stack.append(int(i))
        return stack.pop()