// 二叉树题模板：与 template_tree.py 对应。
use leetcode_hot100::{tree, tree_to_vec, TreeNode};

struct Solution;

// ===== 提交区开始：用 LeetCode 的 impl Solution 替换此处 =====
use std::cell::RefCell;
use std::rc::Rc;

impl Solution {
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        todo!("填入题解；如果换题，也要同步修改下面 main 和 tests 的调用")
    }
}
// ===== 提交区结束 =====

// 思路总结：

fn main() {
    let root = tree![4, 2, 7, 1, 3, 6, 9];
    let result = Solution::invert_tree(root);
    println!("输出结果: {:?}", tree_to_vec(&result));
    assert_eq!(
        tree_to_vec(&result),
        tree_to_vec(&tree![4, 7, 2, 9, 6, 3, 1])
    );
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn sample() {
        let result = Solution::invert_tree(tree![4, 2, 7, 1, 3, 6, 9]);
        assert_eq!(
            tree_to_vec(&result),
            tree_to_vec(&tree![4, 7, 2, 9, 6, 3, 1])
        );
    }

    #[test]
    fn sparse() {
        let result = Solution::invert_tree(tree![1, null, 2, 3]);
        assert_eq!(
            tree_to_vec(&result),
            tree_to_vec(&tree![1, 2, null, null, 3])
        );
    }

    #[test]
    fn empty() {
        assert_eq!(Solution::invert_tree(tree![]), None);
    }
}
