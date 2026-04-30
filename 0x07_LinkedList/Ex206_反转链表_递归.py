from typing import List, Dict, Optional, Set

# Main Logic
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None) or (head.next is None):
            return head
        
        reversed_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return reversed_head

# 思路总结

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
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
    # 构造测试用例
    testcase = []
    
    # 调用方法并打印结果
    result = sol.reverseList(a1)
    print(f"输出结果: {result.next.val}")