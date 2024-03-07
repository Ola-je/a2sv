class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = (len(matrix)*len(matrix[0])) -1

        while left <= right:
            mid = (left + right)//2

            if matrix[mid//len(matrix[0])][mid%len(matrix[0])] == target:
                return True
            elif matrix[mid//len(matrix[0])][mid%len(matrix[0])] < target:
                left = mid+1
            else:
                right = mid-1

        return False