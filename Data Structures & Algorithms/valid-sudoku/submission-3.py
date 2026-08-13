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
        s1 , s2 , s3 , s4 , s5 , s6 , s7 , s8 , s9 = set(),set(),set(),set(),set(),set(),set(),set(),set()
        for l in board[0:3]:
            for m in range(0,3):
                if l[m] in s1 and l[m] != ".":
                    return False
                s1.add(l[m])
        for l in board[0:3]:
            for m in range(3,6):
                if l[m] in s2 and l[m] != ".":
                    return False
                s2.add(l[m])
        for l in board[0:3]:
            for m in range(6,9):
                if l[m] in s3 and l[m] != ".":
                    return False
                s3.add(l[m])
        for l in board[3:6]:
            for m in range(0,3):
                if l[m] in s4 and l[m] != ".":
                    return False
                s4.add(l[m])
        for l in board[3:6]:
            for m in range(3,6):
                if l[m] in s5 and l[m] != ".":
                    return False
                s5.add(l[m])
        for l in board[3:6]:
            for m in range(6,9):
                if l[m] in s6 and l[m] != ".":
                    return False
                s6.add(l[m])
        for l in board[6:9]:
            for m in range(0,3):
                if l[m] in s7 and l[m] != ".":
                    return False
                s7.add(l[m])
        for l in board[6:9]:
            for m in range(3,6):
                if l[m] in s8 and l[m] != ".":
                    return False
                s8.add(l[m])
        for l in board[6:9]:
            for m in range(6,9):
                if l[m] in s9 and l[m] != ".":
                    return False
                s9.add(l[m])
        return True