class Solution:
    def timeRequiredToBuy(self, n: List[int], k: int) -> int:
        count =0
        queue = []
        i =0
        while n[k]> 0:
            if n[i] >0 and n[k] > 0:
                n[i] -=1
                count +=1
            i+=1
            if i == len(n):
                i=0
            
        return count