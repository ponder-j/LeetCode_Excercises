from typing import List, Dict, Optional, Set
from collections import deque

# Main Logic
class Solution:
    # 所谓滑动窗口实际上维护的是从开始到右游标的单调队列
    # 从开始到左游标的数由另外的逻辑剔除
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        monoq = deque() # 维护一个单调递减的队列
        for i, num in enumerate(nums):
            # 队列中末端元素比后来者小，就可以滚蛋了
            print(monoq)
            while monoq and nums[monoq[-1]] <= num:
                monoq.pop()
                print(monoq)
            monoq.append(i) # 加入的是下标，加入值没有意义
            print(monoq)
            while monoq[0] <= i - k: # 判断下标是否超界，超界直接滚蛋
                monoq.popleft()
                print(monoq)
            if i < k - 1: # 前 k - 1 个数还没有形成窗口，不用加入答案
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