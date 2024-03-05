class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []

        def backtrack():
            if len(curr) == len(nums):
                result.append(curr.copy())
                return
            for j in nums:
                if j in curr:
                    continue
                curr.append(j)
                backtrack()
                curr.pop()
        backtrack()
        return result