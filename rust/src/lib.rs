//! LeetCode 本地辅助工具；提交题解时不需要复制这个库。

mod list;
mod tree;

pub use list::{list_from_slice, list_to_vec, ListNode};
pub use tree::{build_tree, tree_to_vec, Tree, TreeNode};

/// 用数组形式构造链表，支持空链表、负数和末尾逗号。
///
/// ```
/// use leetcode_hot100::{list, list_to_vec};
/// assert_eq!(list_to_vec(&list![1, -2, 3]), vec![1, -2, 3]);
/// assert!(list![].is_none());
/// ```
#[macro_export]
macro_rules! list {
    ($($value:expr),* $(,)?) => {
        $crate::list_from_slice(&[$($value),*])
    };
}

/// 用 LeetCode 层序数组构造二叉树，空节点直接写 `null`。
///
/// ```
/// use leetcode_hot100::{tree, tree_to_vec};
/// let root = tree![1, null, -2, 3];
/// assert_eq!(tree_to_vec(&root), vec![Some(1), None, Some(-2), Some(3)]);
/// assert!(tree![].is_none());
/// ```
#[macro_export]
macro_rules! tree {
    (@parse [$($values:expr,)*]) => {
        $crate::build_tree(&[$($values,)*])
    };
    (@parse [$($values:expr,)*] null $(, $($rest:tt)*)?) => {
        $crate::tree!(@parse [$($values,)* None,] $($($rest)*)?)
    };
    (@parse [$($values:expr,)*] $value:expr $(, $($rest:tt)*)?) => {
        $crate::tree!(@parse [$($values,)* Some($value),] $($($rest)*)?)
    };
    ($($values:tt)*) => {
        $crate::tree!(@parse [] $($values)*)
    };
}
