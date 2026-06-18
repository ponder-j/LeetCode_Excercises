from typing import List, Dict, Optional, Set
import sys

dic_n2l = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

def combin(a: str) -> None:
    n = len(a)

    def dfs(sentence: str, step: int):
        if step == n:
            print(sentence)
            return
        
        for letter in dic_n2l[a[step]]:



def main():
    nums = sys.stdin.readline().strip()
    combin(nums)

if __name__ == "__main__":
    main()