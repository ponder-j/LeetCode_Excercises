from typing import List, Dict, Optional, Set
from queue import PriorityQueue

# Main Logic
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        pq = PriorityQueue()
        for i in range(k):
            pq.put((-nums[i], i))
        p = k
        ans = []
        ans.append(-pq.queue[0][0])
        while p < n:
            pq.put((-nums[p], p))
            qmax = pq.queue[0]
            while qmax[1] <= p - k:
                pq.get()
                qmax = pq.queue[0]
            ans.append(-pq.queue[0][0])
            p += 1
        
        return ans
            
            
# 思路总结
# 多个最大值，想到优先队列；然后有一个重要的思想，不要想着立刻把窗口外的除名掉，可以留着，判断 index 是否出界再删掉
# 但这并不是个好方法，这题更应该用单调队列

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    nums = [1,-1]
    k = 1
    
    # 调用方法并打印结果
    result = sol.maxSlidingWindow(nums, k)
    print(f"输出结果: {result}")