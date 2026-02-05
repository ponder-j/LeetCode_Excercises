from typing import List, Dict, Optional, Set

# Main Logic
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max = nums[0]
        for i in range(n):
            
# 思路总结

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = [-2,1,-3,4,-1,2,1,-5,4]
    
    # 调用方法并打印结果
    result = sol.maxSubArray(testcase)
    print(f"输出结果: {result}")