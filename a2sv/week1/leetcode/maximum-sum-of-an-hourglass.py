class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_val = 0
        hourglass = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                hourglass1 = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                hourglass2 = grid[i+1][j+1]
                hourglass3 = grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                hourglass = hourglass1+hourglass2+hourglass3
                max_val = max(max_val,hourglass)
        return max_val