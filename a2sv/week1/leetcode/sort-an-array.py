class Solution:

    def merge_sort(self, nums):

        if len(nums) <= 1:

            return nums


        mid = len(nums) // 2

        left_half = nums[:mid]

        right_half = nums[mid:]


        left_half = self.merge_sort(left_half)

        right_half = self.merge_sort(right_half)

        
        return self.merge(left_half, right_half)

    def merge(self, left, right):

        merged = []

        left_index = 0

        right_index = 0


        while left_index < len(left) and right_index < len(right):

            if left[left_index] <= right[right_index]:

                merged.append(left[left_index])

                left_index += 1

            else:

                merged.append(right[right_index])

                right_index += 1


        while left_index < len(left):

            merged.append(left[left_index])

            left_index += 1


        while right_index < len(right):

            merged.append(right[right_index])

            right_index += 1

        return merged

    def sortArray(self, nums):

        return self.merge_sort(nums)
