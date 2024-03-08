class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = cur_sum = 0
        sum_cnt = {0:1}
        
        for i in nums:
            cur_sum += i 
            if cur_sum - k in sum_cnt:
                res += sum_cnt[cur_sum - k]
                
            if cur_sum in sum_cnt:
                sum_cnt[cur_sum] += 1
            else:
                sum_cnt[cur_sum] = 1
                
        return res