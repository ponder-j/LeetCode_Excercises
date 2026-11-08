/// 字段与 LeetCode 常见 Rust 链表题的定义一致。
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    pub fn new(val: i32) -> Self {
        Self { val, next: None }
    }
}

pub fn list_from_slice(values: &[i32]) -> Option<Box<ListNode>> {
    let mut head = None;
    for &val in values.iter().rev() {
        head = Some(Box::new(ListNode { val, next: head }));
    }
    head
}

/// 借用链表而不消耗它，便于多次打印和断言。
pub fn list_to_vec(head: &Option<Box<ListNode>>) -> Vec<i32> {
    let mut values = Vec::new();
    let mut current = head.as_deref();
    while let Some(node) = current {
        values.push(node.val);
        current = node.next.as_deref();
    }
    values
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn empty_list() {
        assert_eq!(list_from_slice(&[]), None);
        assert!(list_to_vec(&None).is_empty());
        assert_eq!(crate::list![], None);
    }

    #[test]
    fn preserves_order_duplicates_and_negative_values() {
        let head = crate::list![1, -2, -2, 0,];
        assert_eq!(list_to_vec(&head), vec![1, -2, -2, 0]);
        assert_eq!(head.as_ref().unwrap().val, 1);
        assert_eq!(head.as_ref().unwrap().next.as_ref().unwrap().val, -2);
        // 转换没有消耗原链表。
        assert_eq!(list_to_vec(&head), vec![1, -2, -2, 0]);
    }

    #[test]
    fn singleton() {
        assert_eq!(crate::list![42], Some(Box::new(ListNode::new(42))));
    }
}
