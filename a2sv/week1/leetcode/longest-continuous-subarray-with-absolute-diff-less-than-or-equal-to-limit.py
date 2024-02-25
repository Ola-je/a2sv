class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        max_deque = []
        min_deque= []
        longest =0
        l=r=0

        while r<len(nums):
            while max_deque and max_deque[-1] < nums[r]:
                max_deque.pop()
            while min_deque and min_deque[-1] > nums[r]:
                min_deque.pop()
            max_deque.append(nums[r])
            min_deque.append(nums[r])

            while max_deque[0] - min_deque[0] > limit:
                if max_deque[0]==nums[l]:
                    max_deque.pop(0)
                if min_deque[0]==nums[l]:
                    min_deque.pop(0)
                l+=1
           
            longest = max(longest, r-l+1) 
            r+=1
        return longest