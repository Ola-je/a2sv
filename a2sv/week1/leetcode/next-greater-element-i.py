class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = [-1]*len(nums1)
        dic = {num: i for i, num in enumerate(nums2)}
        
        for k, i in dic.items():
            while stack  and stack[-1] < nums2[i]:
                poped_element = stack.pop()
                if poped_element in nums1:
                    ans[nums1.index(poped_element)] = nums2[i]
            stack.append(nums2[i])
        return ans
            
            