class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        curr = []


        def backtrack(i):
            if i >= len(nums):
                result.add(tuple(sorted(curr)))
                return
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()
            backtrack(i+1)
        backtrack(0)
        return result