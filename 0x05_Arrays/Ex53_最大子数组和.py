from typing import List, Dict, Optional, Set

# Main Logic
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        fi = nums[0]
        for i in range(1, n):
            if fi + nums[i] > nums[i]:
                fi = fi + nums[i]
                if fi > ans:
                    ans = fi
            else:
                fi = nums[i]
                if fi > ans:
                    ans = fi
        return ans
        
            
# 思路总结
# 递归思想，定义 f[i] 是以 nums[i] 为结尾的最大子数组和。“以单个元素为结尾的某个相关值”这个思想在 Ex560 中也有体现
# 想到这一点，自然很容易就能想到递推式：f[i] = max{f[i-1] + nums[i], nums[i]} ; f[0] = nums[0]
# 因此只需要以 O(n) 的复杂度扫一遍就行了

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = [1]
    
    # 调用方法并打印结果
    result = sol.maxSubArray(testcase)
    print(f"输出结果: {result}")