class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1   
        count = 1   
        while i>=0:
            digits[i] += count
            count = digits[i] // 10
            digits[i] %= 10
            i-=1
        if count:
            digits.insert(0,count)
        return digits
        