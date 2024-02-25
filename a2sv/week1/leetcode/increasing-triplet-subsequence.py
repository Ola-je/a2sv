class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        num1= float("inf")
        num2= float("inf")
        for i in nums:
            if i <= num1:
                num1= i
            elif i <= num2:
                num2= i
            else:
                return True
        return False