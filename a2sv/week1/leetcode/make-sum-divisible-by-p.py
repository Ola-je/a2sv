class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_rem = sum(nums)%p
        summation = 0
        min_ = len(nums)
        dic = {0: -1}

        if sum(nums) < p:
            return -1

        if total_rem == 0:
            return 0

        for index, num in enumerate(nums):
            summation = (summation + num) % p
            target_mod = (summation - total_rem + p) % p

            if target_mod in dic:
                min_ = min(min_, index - dic[target_mod])
            dic[summation] = index

        return -1 if min_ == len(nums) else min_