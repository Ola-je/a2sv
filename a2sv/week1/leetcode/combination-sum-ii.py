class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        cur = []

        def backtrack(i):
            if sum(cur) == target:
                result.append(cur.copy())
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if sum(cur) + candidates[j] > target:
                    break
                cur.append(candidates[j])
                backtrack(j+1)
                cur.pop()
               
        backtrack(0)
        return result
