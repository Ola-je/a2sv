class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps = list(accumulate(nums))
        count = {0:1}
        result = 0

        for i in ps:
            if i - k in count:
                result += count[i - k]
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        return result 

