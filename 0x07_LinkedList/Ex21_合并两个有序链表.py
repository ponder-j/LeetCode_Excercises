from typing import List, Dict, Optional, Set

# Main Logic
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print_list(self):
        p = self
        while p is not None:
            print(p.val)
            p = p.next

class Solution_rubbish:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        if (p1 is None):
            return p2
        elif (p2 is None):
            return p1
        if p1.val <= p2.val:
            head = ListNode(p1.val)
            p1 = p1.next
        else:
            head = ListNode(p2.val)
            p2 = p2.next
        pre = head
        while (p1 is not None) and (p2 is not None):
            if p1.val <= p2.val:
                pre.next = ListNode(p1.val)
                pre = pre.next
                p1 = p1.next
            else:
                pre.next = ListNode(p2.val)
                pre = pre.next
                p2 = p2.next
        if p1 is not None:
            while p1 is not None:
                pre.next = ListNode(p1.val)
                p1, pre = p1.next, pre.next
        else:
            while p2 is not None:
                pre.next = ListNode(p2.val)
                p2, pre = p2.next, pre.next
        
        return head

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 直接递归
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2

# 思路总结

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(4)

    a4 = ListNode(1)
    a5 = ListNode(3)
    a6 = ListNode(4)

    a1.next = a2
    a2.next = a3

    a4.next = a5
    a5.next = a6
    
    # 调用方法并打印结果
    result = sol.mergeTwoLists(a1, a6)
    print(f"输出结果: {result.print_list()}")