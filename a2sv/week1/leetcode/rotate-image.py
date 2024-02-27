class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols= len(matrix[0])

        l=0
        r=rows-1
        while l<r:
            matrix[l], matrix[r] =matrix[r], matrix[l]
            l+=1
            r-=1
        for i in range(rows):
            for j in range(i+1,cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        