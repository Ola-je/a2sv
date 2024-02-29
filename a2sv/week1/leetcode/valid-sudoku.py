class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            dicCol = {}
            dicRow ={}
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in dicRow:
                        return False
                        break
                    else:
                        dicRow[board[i][j]] = 1
                if board[j][i] != '.':
                    if board[j][i] in dicCol:
                        return False
                        break
                    else:
                        dicCol[board[j][i]] = 1
                if (i == 0 and j == 0) or (i == 3 and j == 0) or (i == 6 and j == 0) or (i == 0 and j == 3) or (i == 0 and j == 6) or  (i == 3 and j == 3) or (i == 3 and j == 6) or (i == 6 and j == 3) or (i == 6 and j == 6):

                    k = i
                    f = j
                    dicCell = {}
                    while k< i+3:
                        while f < j +3:
                            if board [k][f] != '.':
                                if board[k][f] in dicCell:
                                    return False
                                    break 
                                else:
                                    dicCell[board[k][f]] = 1
                            f +=1
                        k +=1
                        f = j
        return True  