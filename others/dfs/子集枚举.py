from typing import List, Dict, Optional, Set
import sys

def subsetEnumeration(a: List) -> None:
    n = len(a)
    
    def dfs(arr: List, see):
        if see == n:
            print(arr)
            return

        # 不取当前元素
        dfs(arr, see + 1)

        # 取当前元素
        arr.append(a[see])
        dfs(arr, see + 1)
        arr.pop()

    
    dfs([], 0)

def main():
    nums = list(map(int, sys.stdin.read().strip().split()))
    subsetEnumeration(nums)

if __name__ == "__main__":
    main()