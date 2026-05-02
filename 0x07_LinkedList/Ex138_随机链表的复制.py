from typing import List, Dict, Optional, Set

# Main Logic
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list2linkedlist(a: List) -> Optional[Node]:
    if not a:
        return None
    head = Node(x=a[0][0], next=None, random=a[0][1])
    p = head
    for num in a[1:]:
        p.next = Node(x=num[0], next=None, random=num[1])
        p = p.next

    return head

def printLinkedlist(a: Optional[Node]):
    if a is None:
        return
    while a is not None:
        print(a.val, end=" -> ")
        a = a.next
    print()

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_dict = {}
        p = head
        if p is None:
            return None
        if p.next is None:
            return Node(x=p.val)
        
        newhead = Node(x=p.val)
        node_dict[p] = newhead
        pnew = newhead
        while p.next is not None:
            pnew.next = Node(x=p.next.val)
            node_dict[p.next] = pnew.next
            p = p.next
            pnew = pnew.next
        
        p = head
        while p.next is not None:
            if p.random is not None:
                node_dict[p].random = node_dict[p.random]
            p = p.next
        
        return newhead


# 思路总结

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = list2linkedlist([[7,None],[13,0],[11,4],[10,2],[1,0]])
    
    # 调用方法并打印结果
    result = sol.copyRandomList(testcase)
    printLinkedlist(testcase)
    printLinkedlist(result)