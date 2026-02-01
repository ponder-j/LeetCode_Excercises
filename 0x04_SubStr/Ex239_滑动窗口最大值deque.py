from typing import List, Dict, Optional, Set
from collections import deque

# Main Logic
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        monoq = deque()
        for i, num in enumerate(nums):
            while monoq and nums[monoq[-1]] <= num:
                monoq.pop()
            monoq.append(i)
            while monoq[0] <= i - k:
                monoq.popleft()
            
            if i < k - 1:
                continue
            ans.append(nums[monoq[0]])
        
        return ans
            
            
# 思路总结
# 维护一个单调队列；一个重要的思想，不要想着立刻把窗口外的除名掉，可以留着，判断 index 是否出界再删掉


# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    
    # 调用方法并打印结果
    result = sol.maxSlidingWindow(nums, k)
    print(f"输出结果: {result}")