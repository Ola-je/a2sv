class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        index =[]
        c_l = c_r = val = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c_r += 1
        for i in range(len(nums)+1):
            x = c_r + c_l
            if i<len(nums):
                if nums[i] == 0:
                    c_l += 1
                else:
                    c_r -= 1
            if x>val:
                index.clear()
                val = x
                index.append(i)
            elif val == x:
                index.append(i)
                
        return index

