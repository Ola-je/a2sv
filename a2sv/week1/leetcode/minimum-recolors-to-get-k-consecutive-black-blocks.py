class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l =0 
        count =0
        result = k

        for r in range(len(blocks)):
            if blocks[r] == 'W':
                count +=1
            while r-l+1 == k:
                result = min(result, count)
                if blocks[l] == 'W':
                    count-=1
                l +=1
        return result
