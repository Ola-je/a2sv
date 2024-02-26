class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak = 0
        while peak < len(arr)-1 and arr[peak] < arr[peak+1]:
            peak +=1
        if peak == 0 or peak == len(arr)-1:
            return False
        while peak < len(arr)-1 and arr[peak] > arr[peak+1]:
            peak +=1
        if peak == len(arr)-1:
            return True
        else:
                return False