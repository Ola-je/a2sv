class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_ = float('-inf')

        while left < right:
            min_ = min(height[left], height[right])
            result = min_ * (right-left)
            max_ = max(max_, result)

            if height[left] <= height[right]:
                left +=1
            else:
                right -=1
        return max_