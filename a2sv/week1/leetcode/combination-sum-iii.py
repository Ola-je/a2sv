class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = set()
        curr =[]

        def backtrack(i):
            if len(curr) == k and sum(curr) == n:
                result.add(tuple(sorted(curr)))
                return
            if sum(curr) > n or len(curr) > k:
                return

            for j in range(i, 10):
                if j > n:
                    break
                
                curr.append(j)
                backtrack(j+1)
                curr.pop()

        backtrack(1)
        return result