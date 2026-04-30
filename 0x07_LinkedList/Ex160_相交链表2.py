from typing import List, Dict, Optional, Set

# Main Logic
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional['ListNode'] = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA, pB = headA, headB
        while pA != pB:
            if pA:
                pA = pA.next
            else:
                pA = headB
            if pB:
                pB = pB.next
            else:
                pB = headA
        
        return pA

# 思路总结
# 我们可以这样设想：
#     设链表 A 不相交的部分长度为 a
#     设链表 B 不相交的部分长度为 b
#     设两个链表相交的部分长度为 c
# 如果你安排两个指针 pA 和 pB 分别从 headA 和 headB 出发：
#     pA 遍历完链表 A 后，让它跳到链表 B 的头部继续遍历。
#     pB 遍历完链表 B 后，让它跳到链表 A 的头部继续遍历。
# 为什么这样有效？
#     pA 到达相交节点时，走过的路程是：a + c + b （走完 A，再走 B 的不相交部分）。
#     pB 到达相交节点时，走过的路程是：b + c + a （走完 B，再走 A 的不相交部分）。
#     因为 a + c + b == b + c + a，所以两个指针必定会同时到达相交的起始节点！
#     如果两个链表完全不相交（即 c = 0），那么 pA 会走过 a + b，pB 也会走过 b + a，最终两人会同时到达各自路径的终点 None，循环结束并返回 None。

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