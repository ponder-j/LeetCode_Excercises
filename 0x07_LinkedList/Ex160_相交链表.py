from typing import List, Dict, Optional, Set

# Main Logic
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional['ListNode'] = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pass_dict = set()
        cur = headA
        while cur is not None:
            pass_dict.add(cur)
            cur = cur.next
        cur = headB
        while cur is not None:
            if cur in pass_dict:
                return cur
            else:
                cur = cur.next
        return None

# 思路总结

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    a1 = ListNode(4)
    a2 = ListNode(1)
    a3 = ListNode(8)
    a4 = ListNode(4)
    a5 = ListNode(5)
    a6 = ListNode(5)
    a7 = ListNode(6)
    a8 = ListNode(1)

    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a6.next = a7
    a7.next = a8
    a8.next = a3
    
    # 调用方法并打印结果
    result = sol.getIntersectionNode(a1, a6)
    print(f"输出结果: {result.val}")