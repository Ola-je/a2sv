class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i=j=0
        ans =0
        while i< len(mat) and j<len(mat):
            ans+= mat[i][j]
            i+=1
            j+=1
        i=0
        j= len(mat)-1
        while i< len(mat) and j>=0:
            ans+= mat[i][j]
            i+=1
            j-=1
        if len(mat)%2 ==1:
            i = (len(mat)-1)//2
            ans-=mat[i][i]
        return ans