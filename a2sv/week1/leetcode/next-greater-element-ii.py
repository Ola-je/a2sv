class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1]*len(nums)
        n =len(nums)

        for i in range(n*2):
            while stack and nums[stack[-1]] < nums[i%n]:
                val = stack.pop()
                result[val] = nums[i%n]
            stack.append(i%n)
                
        return result