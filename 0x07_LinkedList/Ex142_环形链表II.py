from typing import List, Dict, Optional, Set

# Main Logic
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = Optional['ListNode'] = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hasVisited = set()
        p = head
        while p is not None:
            hasVisited.add(p)
            p = p.next
            if p in hasVisited:
                return p
        
        return None

# 思路总结

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = []
    
    # 调用方法并打印结果
    result = sol.fun(testcase)
    print(f"输出结果: {result}")