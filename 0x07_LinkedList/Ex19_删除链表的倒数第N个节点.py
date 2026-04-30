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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fake = ListNode(0, head)
        stack = []
        p = fake
        while p is not None:
            stack.append(p)
            p = p.next
        for i in range(n):
            stack.pop()
        if stack == []:
            return None
        target = stack[-1]
        target.next = target.next.next
        return fake.next

# 思路总结
# 技巧，使用 fake_head 避免分类讨论

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = list2linkedlist([1,2])
    printLinkedlist(testcase)
    
    # 调用方法并打印结果
    result = sol.removeNthFromEnd(testcase, n=1)
    # print(f"输出结果: {result}")
    printLinkedlist(result)