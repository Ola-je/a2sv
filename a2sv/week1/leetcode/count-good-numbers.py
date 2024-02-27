class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        def mypow(base,exponent):
            ans = 1
            while exponent > 0:
                if exponent%2==1:
                    ans =(ans *base)%mod
                base = (base*base)%mod
                exponent//=2
            return ans
        even = mypow(5, n//2 + n%2)
        odd = mypow(4, n//2)
            
        return (even*odd)%mod