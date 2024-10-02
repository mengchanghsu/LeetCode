"""
LeetCode 37 - https://leetcode.com/problems/sudoku-solver/description/
Author's github: https://github.com/mengchanghsu/LeetCode.git
回溯法：這是一種常見的解決約束滿足問題的方法。通過逐步嘗試不同的選擇來尋找解決方案，如果發現某個選擇無法達成目標，就回退到上一步重新選擇。
"""
from typing import List
import time

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def isValid(board, row, col, num):
            # 檢查行
            for c in range(9):
                if board[row][c] == num:
                    return False
            # 檢查列
            for r in range(9):
                if board[r][col] == num:
                    return False
            # 檢查 3x3 子區域
            startRow, startCol = 3 * (row // 3), 3 * (col // 3)
            for r in range(startRow, startRow + 3):
                for c in range(startCol, startCol + 3):
                    if board[r][c] == num:
                        return False
            return True
    
        def solve(board):
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for num in map(str, range(1, 10)):
                            if isValid(board, r, c, num):
                                board[r][c] = num  # 做選擇
                                if solve(board):
                                    return True
                                board[r][c] = '.'  # 撤銷選擇
                        return False  # 無法填寫，需回退
            return True  # 解決成功

        # Run
        start_time = time.time()  # 計時開始
        solve(board)
        end_time = time.time()  # 計時結束
        elapsed_time = end_time - start_time  # 計算運行時間
        print(board)
        print(f'Solve Sudoku finished!! 程式運行時間: {elapsed_time:.5f} 秒')


"""
example,這段不用貼到LeetCode
"""
sol = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
result = sol.solveSudoku(board)

board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
result = sol.solveSudoku(board)