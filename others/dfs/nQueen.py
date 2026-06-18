from typing import List, Dict, Optional, Set
import sys

num = int(sys.stdin.readline().strip())
board = [[False for _ in range(num)] for _ in range(num)]

def nQueenSol(n: int) -> int:
    methods = []

    def outofboard(i: int, j: int) -> bool:
        if i < 0 or i >= n or j < 0 or j >= n:
            return True
        return False
    
    def useit(i: int, j: int):

        for line in range(n):
            board[line][j] = True
        for row in range(n):
            board[i][row] = True

        line, row = i, j
        while not outofboard(line, row):
            board[line][row] = True
            line += 1
            row += 1
        
        line, row = i, j
        while not outofboard(line, row):
            board[line][row] = True
            line += 1
            row -= 1
        
        line, row = i, j
        while not outofboard(line, row):
            board[line][row] = True
            line -= 1
            row += 1
        
        line, row = i, j
        while not outofboard(line, row):
            board[line][row] = True
            line -= 1
            row -= 1

    def dfs(map: List[int], cur_line: int) -> None:
        global board
        if cur_line == n:
            methods.append(map)
            return
        
        for i in range(n):
            if board[cur_line][i] == False:
                backup = [[board[i][j] for i in range(n)] for j in range(n)]
                useit(cur_line, i)
                map.append(i)
                dfs(map, cur_line + 1)
                map.pop()
                board = [[backup[i][j] for i in range(n)] for j in range(n)]

    dfs([], 0)
    return len(methods)


def main():
    print(nQueenSol(num))

if __name__ == "__main__":
    main()