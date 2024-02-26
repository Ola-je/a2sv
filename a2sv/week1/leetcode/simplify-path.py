class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split('/')

        for n in components:
            if n == '.' or not n:
                continue
            elif n == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(n)
        return '/' + '/'.join(stack)