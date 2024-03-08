class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def checker(radius):
            i = j = 0
            while i < len(houses):
                if j>= len(heaters) or  houses[i] < heaters[j]-radius:
                    return False
                if houses[i] > heaters[j] + radius:
                    j += 1
                else:
                    i+=1
            return True

        l, r = 0, int(1e9)

        while l<=r:
            mid = (l+r)//2
            if checker(mid):
                r = mid -1
            else:
                l = mid+1
        return l