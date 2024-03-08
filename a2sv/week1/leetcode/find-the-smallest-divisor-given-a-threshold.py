class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        m = max(nums)
        if threshold == len(nums):
            return m

        def checker(num):
            sum = 0
            for i in nums:
                sum += ceil(i/num)
            return sum

        l, r = 1, m
        while l<=r:
            mid = (l+r)//2
            if checker(mid) > threshold:
                l = mid+1
            else:
                r = mid-1
        return l
        