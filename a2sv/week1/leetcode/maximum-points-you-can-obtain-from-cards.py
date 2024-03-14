class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        
        first = sum(cardPoints[:k])
        ans = first
        second = 0
        right = len(cardPoints)-1

        for i in range(k-1, -1, -1):
            second += cardPoints[right]
            first -= cardPoints[i]
            ans = max(ans, second+first)
            right -= 1
        return ans
