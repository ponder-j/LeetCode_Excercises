from typing import List, Dict, Optional, Set
import sys

def fullPermutation(a: List) -> None:
    n = len(a)
    used = [0 for _ in range(n)]

    def dfs(arr: List, cur_len: int) -> None:
        if cur_len == n:
            print(arr)
            return
        
        for i in range(n):
            if used[i] == 0:
                used[i] = 1
                arr.append(a[i])
                dfs(arr, cur_len + 1)
                arr.pop()
                used[i] = 0
    
    dfs([], 0)

def main():
    nums = list(map(int, sys.stdin.read().strip().split()))
    fullPermutation(nums)

if __name__ == "__main__":
    main()