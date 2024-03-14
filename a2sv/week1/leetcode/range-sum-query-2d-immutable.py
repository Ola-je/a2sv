class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rnum = len(matrix)+1
        self.cnum = len(matrix[0])+1

        self.ps_matrix = [[0] * self.cnum for _ in range(self.rnum)]

        for i in range(self.rnum-1):
            for j in range(self.cnum-1):
                self.ps_matrix[i+1][j+1] = self.ps_matrix[i+1][j] + self.ps_matrix[i][j+1] - self.ps_matrix[i][j] + matrix[i][j]
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return (self.ps_matrix[row1][col1] - self.ps_matrix[row1][col2+1] -self.ps_matrix[row2+1][col1] + self.ps_matrix[row2+1][col2+1])



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)