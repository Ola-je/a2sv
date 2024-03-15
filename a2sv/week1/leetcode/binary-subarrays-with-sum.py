class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        psum = list(accumulate(nums))
        result =0
        count = {0:1}

        for i in psum:
            if i - goal in count:
                result += count[i-goal]
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        return result
        