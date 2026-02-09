from typing import List, Dict, Optional, Set

# Main Logic
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # lpro = []
        n = len(nums)
        rpro = [1 for i in range(n)]
        ans = [1 for i in range(n)]
        for i in range(n-2, -1, -1):
            rpro[i] = nums[i+1] * rpro[i+1]
        templpro = 1
        for i in range(n):
            ans[i] = templpro * rpro[i]
            templpro *= nums[i]
        return ans

# 思路总结
# 类似前缀和/动态规划的思路，记录部分乘积，避免重复运算
# testcase = [1,2,3,4]
# 计算 rpro （当前位置右边的所有数的乘积）= [24,12,4,1]

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = [1,2,3,4]
    
    # 调用方法并打印结果
    result = sol.productExceptSelf(testcase)
    print(f"输出结果: {result}")