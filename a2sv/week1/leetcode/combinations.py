class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(idx, comb):
            if len(comb) == k:
                result.append(comb.copy())
                return 
            
            for i in range(idx, n+1):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()
        backtrack(1, [])
        return result 