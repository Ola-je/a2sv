class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        x = math.log10(n) / math.log10(4)
        return x.is_integer()