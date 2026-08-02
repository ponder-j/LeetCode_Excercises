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
# 优化：传递下标而不是传递列表
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {val:index for index, val in enumerate(inorder)}

        def build_tree(preo_s, preo_e, ino_s, ino_e) -> Optional[TreeNode]:
            if preo_s == preo_e:
                return None
            if preo_e - preo_s == 1:
                return TreeNode(preorder[preo_s])
            
            root_val = preorder[preo_s]
            find_index = index_map[root_val]
            n_left  = find_index
            # n_right = len(ino) - find_index - 1
            new_ino_left  = (ino_s, find_index)
            new_ino_right = (find_index+1, ino_e)

            node  = TreeNode(root_val)
            left  = build_tree(preo_s+1, preo_s+(n_left-ino_s)+1, new_ino_left[0], new_ino_left[1])
            right = build_tree(preo_s+(n_left-ino_s)+1, preo_e, new_ino_right[0], new_ino_right[1])
            node.left  = left
            node.right = right

            return node

        return build_tree(0, len(preorder), 0, len(inorder))


# 思路总结

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    preorder = [3,9,20,15,7]
    inorder  = [9,3,15,20,7]
    # test_root = build_tree(testcase)
    
    # 调用方法并打印结果
    result = sol.buildTree(preorder, inorder)
    print(f"输出结果: {serialize_tree(result)}")