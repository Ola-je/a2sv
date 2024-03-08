class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        if len(piles) == h:
            return m
        
        def checker(speed):
            total_hrs = 0
            for i in piles:
                total_hrs += ceil(i/speed)
            return total_hrs

        l, r = 1, m
        while l<=r:
            mid = (l+r)//2
            if checker(mid) <= h:
                r =mid-1
            else:
                l = mid+1
        return l  
