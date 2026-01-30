from typing import List, Dict, Optional, Set
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        start = 0
        for i in range(len(nums)-1):
            if nums[i] != 0:
                start = i + 1
                continue
            if nums[i+1] != 0:
                nums[start], nums[i+1] = nums[i+1], nums[start]
                start += 1
                continue

def moveZeroes(nums):
    zerop = 0
    for nzerop in range(len(nums)):
        if nums[nzerop] != 0:
            nums[zerop], nums[nzerop] = nums[nzerop], nums[zerop]
            zerop += 1
    print(nums)

moveZeroes([0,1,0,3,0,12])