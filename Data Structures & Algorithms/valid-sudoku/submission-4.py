#Loop 3x3 checking
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Row
        for i in range(len(board)):
            hashmap = set()
            for a in board[i]:
                if a in hashmap and a != ".":
                    return False
                hashmap.add(a)
        #Column
        for k in range(0,9):
            column = set()
            for b in range(len(board)):
                if board[b][k] in column and board[b][k] != ".":
                    return False
                column.add(board[b][k])
        #Square
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):

                seen = set()

                for r in range(start_row, start_row + 3):
                    for c in range(start_col, start_col + 3):

                        if board[r][c] == ".":
                            continue

                        if board[r][c] in seen:
                            return False

                        seen.add(board[r][c])
        return True