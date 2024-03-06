class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        def checker(capacity):
            count = 1
            summation = 0
            for w in weights:
                summation += w
                if summation > capacity:
                    count +=1
                    summation = w
            if count <= days:
                return True
            return False


        while left <= right:
            mid = (left+right)//2

            if checker(mid):
                right = mid - 1
            else:
                left = mid+1
        return left

        





                