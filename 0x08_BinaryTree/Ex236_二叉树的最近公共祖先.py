from collections import deque
from typing import List, Optional, Union, Any, Sequence

class TreeNode:
    """
    二叉树节点定义。
    """
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self) -> str:
        return f"TreeNode({self.val})"

def build_tree(vals: Sequence[Union[int, str, None]]) -> Optional[TreeNode]:
    """
    根据 LeetCode 风格的层序遍历数组构建二叉树。

    同时兼容 Python 原生的 `None` 以及字符串形式的 `"null"` / `"Null"`。
    使用 Sequence 而非 List 来接收参数，从而允许传入不可变的类型并解决协变(Covariant)导致的 Pylance 报错。

    :param vals: 层序遍历值的序列（末尾省略的 null 节点已忽略）
    :return: 构建好的二叉树的根节点
    """
    if not vals:
        return None

    # 处理根节点，如果根节点为空或者为 null 字符串，则返回空树
    if vals[0] is None or (isinstance(vals[0], str) and vals[0].lower() == "null"):
        return None

    # 根节点的值现在可以确定为数字类型
    root = TreeNode(int(vals[0]))
    
    # 队列中只存放已经创建，但还等待挂载子节点的 TreeNode
    queue: deque[TreeNode] = deque([root])
    
    i = 1
    n = len(vals)
    
    while queue and i < n:
        curr = queue.popleft()
        
        # 处理左子节点
        if i < n:
            val_left = vals[i]
            # 如果不是 None，也不是字符串 'null'
            if val_left is not None and not (isinstance(val_left, str) and val_left.lower() == "null"):
                curr.left = TreeNode(int(val_left))
                queue.append(curr.left)
            i += 1
            
        # 处理右子节点
        if i < n:
            val_right = vals[i]
            # 如果不是 None，也不是字符串 'null'
            if val_right is not None and not (isinstance(val_right, str) and val_right.lower() == "null"):
                curr.right = TreeNode(int(val_right))
                queue.append(curr.right)
            i += 1
            
    return root

def serialize_tree(root: Optional[TreeNode]) -> List[Any]:
    """
    将二叉树转换回 LeetCode 风格的层序遍历列表，并自动切除末尾多余的 None。
    用于验证序列化与反序列化的准确性。
    """
    if not root:
        return []

    result: List[Any] = []
    # 显式声明 queue 可以包含 TreeNode 或 None，避免 Pylance 报错
    queue: deque[Optional[TreeNode]] = deque([root])

    while queue:
        curr = queue.popleft()
        if curr:
            result.append(curr.val)
            # 无论叶子节点是否为空，都加入队列等待处理，直到整层结束
            queue.append(curr.left)
            queue.append(curr.right)
        else:
            result.append(None)
            
    # 去除末尾的 None 节点，符合 LeetCode 规范
    while result and result[-1] is None:
        result.pop()
        
    return result

# Solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

# 思路总结

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = [3,5,1,6,2,0,8,"null","null",7,4]
    test_root = build_tree(testcase)
    if test_root is None:
        test_root = TreeNode(0)
    if test_root.left is None:
        test_root.left = TreeNode(0)
    if test_root.right is None:
        test_root.right = TreeNode(0)
    
    # 调用方法并打印结果
    result = sol.lowestCommonAncestor(root=test_root, p=test_root.left, q=test_root.right)
    print(f"输出结果: {result.val}")