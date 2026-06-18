import sys
from typing import List

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cnt = 0

def calcIsland(imap: List[List[int]]) -> int:
    lines = len(imap)
    rows = len(imap[0])

    def dfs(cur_map, x, y):
        global cnt
        for i in range(lines):
            for j in range(rows):
                # 遇到陆地，使用 dfs 将所有邻接的陆地都沉没掉
                if cur_map[i][j] == 1:
                    cnt += 1
                    for dir in directions:
                        if i + dir[0] < 0 or i + dir[0] > lines - 1 or j + dir[1] < 0 or j + dir[1] > rows - 1:
                            return
                        return
    
    dfs(imap, 0, 0)
    return cnt

def main():
    imap = []
    for line in sys.stdin:
        c = line.strip()
        imap.append(list(map(int, c.split())))
    
    print(imap)

if __name__ == "__main__":
    main()