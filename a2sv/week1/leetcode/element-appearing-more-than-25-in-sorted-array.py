class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic = Counter(arr)
        max_val = val =0
        for i in dic:
            if dic[i] > max_val:
                max_val = max(dic[i], max_val)
                val = i

        return val
        