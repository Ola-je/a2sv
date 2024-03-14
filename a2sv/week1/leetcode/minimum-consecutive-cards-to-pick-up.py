class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        max_ = inf
        dic = {}
        for r, x in enumerate(cards):
            if x in dic:
                max_ = min(max_, r-dic[x]+1)
            dic[x] = r
            
        return -1 if max_ == inf else max_
