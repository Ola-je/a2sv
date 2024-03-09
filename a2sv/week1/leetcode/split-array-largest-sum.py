class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        def checker(largest_sum):
            count = 1
            summation = 0
            for num in nums:
                summation += num
                if summation > largest_sum:
                    count += 1
                    summation = num
            return True if count <= k else False
            
        while left <= right:
            mid =(left+right)//2
            if checker(mid):
                right = mid-1
            else:
                left = mid+1
        return left