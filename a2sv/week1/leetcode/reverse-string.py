class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)-1
        left = 0
        right = n
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1