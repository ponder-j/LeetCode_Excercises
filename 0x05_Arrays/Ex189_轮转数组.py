from typing import List, Dict, Optional, Set

# Main Logic
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.reverse()
        k %= n
        for i in range(0, k//2):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]
        for i in range(k, (k + n - 1) // 2 + 1):
            nums[i], nums[k+n-1-i] = nums[k+n-1-i], nums[i]

# 思路总结
# 神秘规律：以测试用例为例，初始数组是
# [1,2,3,4,5,6,7]
# 转完以后数组是
# [5,6,7,1,2,3,4]
# 而初始数组的逆序是
# [7,6,5,4,3,2,1]
# 观察到旋转完和翻转完的初始数组均可以以 3 为界分成两部分，每一个部分分别是对方的逆序

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    nums = [1,2,3,4,5,6,7]
    k = 3
    
    # 调用方法并打印结果
    result = sol.rotate(nums, k)
    print(f"输出结果: {nums}")