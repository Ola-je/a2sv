class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        if len(nums) == k:
            return nums  

        for num, freq in dic.items():
            buckets[freq].append(num)

        res =[]

        for bucket in reversed(buckets):
            if not buckets:
                continue
            for num in bucket:
                if len(res)== k:
                    return res
                res.append(num)
            
       
        return res