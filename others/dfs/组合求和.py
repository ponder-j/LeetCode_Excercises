from typing import List, Dict, Optional, Set
import sys

def chooseSum(a: List[int], target: int) -> None:
    a.sort()
    n = len(a)
    
    def dfs(arr: List[int], cur_sum: int, start: int):
        if cur_sum == target:
            print(arr)
            return
        
        for i in range(start, n):
            # 加最小的一个都爆，那就没必要试后面的了
            if cur_sum + a[i] > target:
                return

            arr.append(a[i])
            dfs(arr, cur_sum + a[i], i)
            arr.pop()

    dfs([], 0, 0)

def main():
    target = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    chooseSum(nums, target)

if __name__ == "__main__":
    main()