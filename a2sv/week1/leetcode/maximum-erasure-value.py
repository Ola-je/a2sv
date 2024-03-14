class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        l=0
        result =0

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                while nums[i] in seen:
                    seen.remove(nums[l])
                    l+=1
                seen.add(nums[i])
            result = max(result, sum(nums[l:i+1]))
        return result  