class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        diagonal = []
        dic = defaultdict(list)
        for i in range(n):
            for j in range(m):
                dic[i+j].append(mat[i][j])
        for x in range(n+m-1):
            if x % 2==0:
                diagonal.extend(dic[x][::-1])
            else:
                diagonal.extend(dic[x])
        return diagonal

