class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        n = len(numbers)
        left, right = 0, n-1
        while left < right and right < n:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                res.append(left + 1)
                res.append(right +1)
                break
        return res