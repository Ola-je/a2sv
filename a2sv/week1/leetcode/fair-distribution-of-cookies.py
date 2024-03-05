class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child =[0]*k  
        min_ = float('inf')


        def backtrack(i, child):
            nonlocal min_

            if i>= len(cookies):
                max_ = max(child)
                min_ =  min(min_, max_)
                return
            for j in range(k):
                child[j] += cookies[i]
                backtrack(i+1, child)
                child[j] -=cookies[i]

                if child[j] == 0:
                    break


        backtrack(0,child)
        return min_