// 普通题模板：复制到 src/bin/p题号_英文名.rs。
struct Solution;

// ===== 提交区开始：用 LeetCode 的 impl Solution 替换此处 =====
#[allow(unused_imports)]
use std::collections::{BinaryHeap, HashMap, HashSet, VecDeque};

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        todo!("填入题解；如果换题，也要同步修改下面 main 和 tests 的调用")
    }
}
// ===== 提交区结束 =====

// 思路总结：

fn main() {
    let nums = vec![2, 7, 11, 15];
    let target = 9;
    let result = Solution::two_sum(nums, target);
    println!("输出结果: {result:?}");
    assert_eq!(result, vec![0, 1]);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn sample() {
        assert_eq!(Solution::two_sum(vec![2, 7, 11, 15], 9), vec![0, 1]);
    }
}
