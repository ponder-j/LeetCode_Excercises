import sys
from typing import List

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def calcIsland(imap: List[List[int]]) -> int:
    cnt = 0

    lines = len(imap)
    rows = len(imap[0])

    def dfs(cur_map, i, j):
        for dir in directions:
            if i + dir[0] < 0 or i + dir[0] > lines - 1 or j + dir[1] < 0 or j + dir[1] > rows - 1:
                continue
            if cur_map[i+dir[0]][j+dir[1]] == 1:
                cur_map[i+dir[0]][j+dir[1]] = 0
                dfs(cur_map, i+dir[0], j+dir[1])

    for i in range(lines):
        for j in range(rows):
            # 遇到陆地，使用 dfs 将所有邻接的陆地都沉没掉
            if imap[i][j] == 1:
                cnt += 1
                dfs(imap, i, j)
                        
    return cnt

def main():
    imap = []
    for line in sys.stdin:
        c = line.strip()
        imap.append(list(map(int, c.split())))
    
    print(calcIsland(imap))

if __name__ == "__main__":
    main()