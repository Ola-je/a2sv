class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        dic = {0:1}
        
        for n in nums:
            prefix_sum += n
            res = prefix_sum % k
            if res in dic:
                count += dic[res]
                dic[res] += 1
            else:
                dic[res] = 1
                
        return count