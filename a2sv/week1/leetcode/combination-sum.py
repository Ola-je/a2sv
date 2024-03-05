class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        st = set()
        def backtrack(i):
            nonlocal target
            if sum(curr) == target:
                result.append(curr.copy())
                st.add(tuple(sorted(curr)))
                return
            if sum(curr) > target:
                return

            for j in range(i, len(candidates)):
                curr.append(candidates[j])
                backtrack(i)
                curr.pop()
        backtrack(0)
        return st

