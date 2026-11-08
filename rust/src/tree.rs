use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

pub type Tree = Option<Rc<RefCell<TreeNode>>>;

/// 字段与 LeetCode 常见 Rust 二叉树题的定义一致。
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Tree,
    pub right: Tree,
}

impl TreeNode {
    pub fn new(val: i32) -> Self {
        Self {
            val,
            left: None,
            right: None,
        }
    }
}

/// 从 LeetCode 层序数组构造树，`None` 表示 null。
/// 空节点不再分配子节点位置，例如 [1, null, 2, 3] 中 3 是 2 的左孩子。
/// 输入应是合法的树；没有父节点的非空值会触发 panic。
pub fn build_tree(values: &[Option<i32>]) -> Tree {
    let mut values = values.iter().copied();
    let root = values
        .next()
        .flatten()
        .map(|val| Rc::new(RefCell::new(TreeNode::new(val))));
    let mut queue = VecDeque::new();
    if let Some(node) = &root {
        queue.push_back(Rc::clone(node));
    }

    while let Some(node) = queue.pop_front() {
        let mut node = node.borrow_mut();
        let TreeNode { left, right, .. } = &mut *node;
        for child in [left, right] {
            if let Some(Some(val)) = values.next() {
                let next = Rc::new(RefCell::new(TreeNode::new(val)));
                queue.push_back(Rc::clone(&next));
                *child = Some(next);
            }
        }
    }
    assert!(values.all(|val| val.is_none()), "存在没有父节点的非空节点");
    root
}

/// 转回层序数组，保留中间的空节点并去掉末尾多余的空节点。
/// 仅用于无环二叉树；借用输入，不修改树。
pub fn tree_to_vec(root: &Tree) -> Vec<Option<i32>> {
    let mut result = Vec::new();
    let mut queue = VecDeque::from([root.clone()]);
    while let Some(node) = queue.pop_front() {
        match node {
            Some(node) => {
                let node = node.borrow();
                result.push(Some(node.val));
                queue.push_back(node.left.clone());
                queue.push_back(node.right.clone());
            }
            None => result.push(None),
        }
    }
    while result.last() == Some(&None) {
        result.pop();
    }
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn empty_tree() {
        assert!(build_tree(&[]).is_none());
        assert!(crate::tree![null].is_none());
        assert!(crate::tree![].is_none());
        assert!(tree_to_vec(&None).is_empty());
    }

    #[test]
    fn sparse_tree_uses_leetcode_level_order() {
        let root = crate::tree![1, null, 2, 3];
        let node = root.as_ref().unwrap().borrow();
        assert!(node.left.is_none());
        let right = node.right.as_ref().unwrap().borrow();
        assert_eq!(right.left.as_ref().unwrap().borrow().val, 3);
        assert_eq!(tree_to_vec(&root), vec![Some(1), None, Some(2), Some(3)]);
    }

    #[test]
    fn round_trip_trims_only_trailing_nulls() {
        let values = [Some(-10), Some(9), Some(20), None, None, Some(15), Some(7)];
        let root = crate::tree![-10, 9, 20, null, null, 15, 7, null, null,];
        assert_eq!(tree_to_vec(&root), values);
        assert_eq!(tree_to_vec(&build_tree(&values)), values);
    }

    #[test]
    fn macro_accepts_expressions() {
        let value = 5;
        assert_eq!(
            tree_to_vec(&crate::tree![value + 1, -value]),
            vec![Some(6), Some(-5)]
        );
    }

    #[test]
    #[should_panic(expected = "没有父节点")]
    fn rejects_orphan_nodes() {
        build_tree(&[Some(1), None, None, Some(2)]);
    }
}
