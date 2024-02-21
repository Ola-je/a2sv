class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic_r = {}
        total = 0
        for i in answers:
            if i in dic_r:
                dic_r[i] += 1
            else:
                dic_r[i] = 1
        for i, count in dic_r.items():
            groups = count // (i + 1)
            remaining = count % (i + 1)
            total += (groups + (1 if remaining > 0 else 0)) * (i + 1)
        return total