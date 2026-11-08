// 1. 两数之和：一个完整示例，用于确认运行、测试和断点调试环境。
struct Solution;

// ===== 提交区开始（包含题解需要的标准库 import） =====
use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen = HashMap::new();
        for (index, value) in nums.into_iter().enumerate() {
            if let Some(&previous) = seen.get(&(target - value)) {
                return vec![previous as i32, index as i32];
            }
            seen.insert(value, index);
        }
        unreachable!("题目保证存在唯一解")
    }
}
// ===== 提交区结束 =====

// 思路总结：扫描数组，用哈希表记录已经出现的数字及其下标。

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
    fn examples() {
        assert_eq!(Solution::two_sum(vec![2, 7, 11, 15], 9), vec![0, 1]);
        assert_eq!(Solution::two_sum(vec![3, 2, 4], 6), vec![1, 2]);
        assert_eq!(Solution::two_sum(vec![3, 3], 6), vec![0, 1]);
    }

    #[test]
    fn negative_values() {
        assert_eq!(Solution::two_sum(vec![-3, 4, 3, 90], 0), vec![0, 2]);
    }
}
