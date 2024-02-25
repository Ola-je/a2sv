class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        l = [-1]*len(arr)
        r = [len(arr)]*len(arr)
        stack=[]
        mod = 10**9 +7
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                val = stack.pop()
                r[val] = i
            stack.append(i)
        stack = []
        for i in range(len(arr)-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                val = stack.pop()
                l[val]=i
            stack.append(i)
        for i in range(len(arr)):
            r[i] -=i
            l[i] = i-l[i]
            ans +=r[i]*l[i]*arr[i]

        return ans%mod