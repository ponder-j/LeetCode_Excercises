from typing import List, Dict, Optional, Set

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        elif (root.left is None) and (root.right is None):
            return 1
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

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