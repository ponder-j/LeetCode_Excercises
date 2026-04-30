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
    for num in a[1:]:
        p.next = ListNode(num)
        p = p.next

    return head

def printLinkedlist(a: Optional[ListNode]):
    if a is None:
        return
    while a is not None:
        print(a.val, end=" -> ")
        a = a.next
    print()

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        # newhead 在第 k 个位置
        newhead = head
        for _ in range(k-1):
            if newhead is None:
                return head
            if newhead.next is None:
                return head
            newhead = newhead.next

        # newend 为原来的 head
        # newend 接入下面已经 reverseKGroup 过的剩余链表
        newend = head
        # newend.next = self.reverseKGroup(newhead.next, k)

        # 接下来翻转当前 K 个元素的链表
        pre = head
        p = head.next

        newend.next = self.reverseKGroup(newhead.next, k)
        
        for _ in range(k-1):
            ne = p.next
            p.next = pre
            pre = p
            p = ne

        return newhead

# 思路总结

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = list2linkedlist([1,2,3,4,5])
    
    # 调用方法并打印结果
    result = sol.reverseKGroup(testcase, k=2)
    printLinkedlist(result)