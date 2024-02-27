class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        result = 0
        turned_on = 0

        for i, flip in enumerate(flips,1):
            turned_on = max(turned_on, flip)
            if turned_on == i:
                result +=1
        return result