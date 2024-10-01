"""
LeetCode 37
https://leetcode.com/problems/sudoku-solver/description/
Author's github: https://github.com/mengchanghsu/LeetCode.git
"""
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        import time
        start_time = time.time()  # 計時開始
        
        # 掃描題目,建立空格列表
        SpaceList = self.createSpaceList(board)

        # 解題
        sn = 0
        for z in range(15):
            if len(SpaceList) == 0 :
                end_time = time.time()  # 計時結束
                elapsed_time = end_time - start_time  # 計算運行時間
                print(board)
                print(f'Solve Sudoku finished!! Use {sn} steps. 程式運行時間: {elapsed_time:.5f} 秒')
                return 
            
            for ix in SpaceList:
                sn += 1
                # print(sn, ix)
                
                i = int(ix.split('-')[1][0])
                j = int(ix.split('-')[1][1])
                if self.writeBoard(i, j, board):
                    # print(f'find 1 answer! {i}{j}')
                    SpaceList.remove(ix)
                else:
                    pass
    
            # # 查看解題狀況
            # print(SpaceList)
            # self.showBoard(board)

    """
    輔助函數
    """
    # 印出目前的數獨矩陣
    def showBoard(self, board):
        for i in range(9):
            print(board[i])
    
    # 輸入i,j，輸出該格子所屬的九宮格數字有哪些
    def subboxes(self, i, j, board):
        sect_x = list(range(int(i / 3) * 3, (int(i / 3) + 1) * 3))
        sect_y = list(range(int(j / 3) * 3, (int(j / 3) + 1) * 3))
        arr = []
        for x in sect_x:
            for y in sect_y:
                arr.append(board[x][y])
        return arr
    
    # 輸入i,j，找出候選數字
    def possibilityNum(self, i, j, board):
        all_unm = ['1','2','3','4','5','6','7','8','9']
        row = board[i]
        column = [board[x][j] for x in range(9)]
        cell = self.subboxes(i, j, board)
        posNum = list(set(all_unm) - set(row) - set(column) - set(cell))
        return posNum

    # 掃描題目,建立空格列表,格式:k-ij,k為候選數字數量
    def createSpaceList(self, board):
        space_list = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    posNum = self.possibilityNum(i, j, board)
                    space_list.append(f'{len(posNum)}-{i}{j}')
        return sorted(space_list)

    # 輸入i,j，嘗試解題，若只有一個候選數字就填入board，其餘跳過
    def writeBoard(self, i, j, board):
        posNum = self.possibilityNum(i, j, board)
        if len(posNum) == 1:
            board[i][j] = posNum[0]
            return True
        else:
            return False

"""
Run,這段不用貼到LeetCode
"""
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
sol = Solution()
result = sol.solveSudoku(board)