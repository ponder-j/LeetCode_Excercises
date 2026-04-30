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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        newhead = head.next
        head.next = self.swapPairs(newhead.next)
        newhead.next = head
        return newhead


# 思路总结
# 依旧递归

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = list2linkedlist([1,2,3,4])
    
    # 调用方法并打印结果
    result = sol.swapPairs(testcase)
    printLinkedlist(result)