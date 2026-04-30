from typing import List, Dict, Optional, Set

# Main Logic
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list2linkedlist(a: List) -> Optional[ListNode]:
    if not a:
        return None
    head = ListNode(a[0])
    p = head
    for num in a:
        p.next = ListNode(num)
        p = p.next

    return head

def printLinkedlist(a: Optional[ListNode]):
    if a is None:
        return
    while a is not None:
        print(a.val, end=" -> ")
        a = a.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        sum = l1.val + l2.val
        take = 0
        if sum >= 10:
            take = 1
            sum -= 10
        head = ListNode(sum)
        p = head

        while (l1.next is not None) and (l2.next is not None):
            sum = l1.next.val + l2.next.val + take
            take = 0
            if sum >= 10:
                take = 1
                sum -= 10
            p.next = ListNode(sum)
            p = p.next
            l1, l2 = l1.next, l2.next
        
        if l1.next is not None:
            sum = l1.next.val + take
            take = 0
            if sum >= 10:
                take = 1
                sum -= 10
            p.next = ListNode(sum)
            p, l1 = p.next, l1.next
        elif l2.next is not None:
            sum = l2.next.val + take
            take = 0
            if sum >= 10:
                take = 1
                sum -= 10
            p.next = ListNode(sum)
            p, l2 = p.next, l2.next
        
        if take == 1:
            p.next = ListNode(1)

        return head
# 思路总结

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    list1 = [9,9,9,9,9,9,9]
    list2 = [9,9,9,9]
    l1 = list2linkedlist(list1)
    l2 = list2linkedlist(list2)
    
    # 调用方法并打印结果
    result = sol.addTwoNumbers(l1, l2)
    # print(f"输出结果: {result}")
    printLinkedlist(result)