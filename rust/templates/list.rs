// 链表题模板：与 template_link.py 对应。
use leetcode_hot100::{list, list_to_vec, ListNode};

struct Solution;

// ===== 提交区开始：用 LeetCode 的 impl Solution 替换此处 =====
impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        todo!("填入题解；如果换题，也要同步修改下面 main 和 tests 的调用")
    }
}
// ===== 提交区结束 =====

// 思路总结：

fn main() {
    let head = list![1, 2, 3, 4, 5];
    let result = Solution::reverse_list(head);
    println!("输出结果: {:?}", list_to_vec(&result));
    assert_eq!(list_to_vec(&result), vec![5, 4, 3, 2, 1]);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn sample() {
        let result = Solution::reverse_list(list![1, 2, 3, 4, 5]);
        assert_eq!(list_to_vec(&result), vec![5, 4, 3, 2, 1]);
    }

    #[test]
    fn empty() {
        assert_eq!(Solution::reverse_list(list![]), None);
    }
}
