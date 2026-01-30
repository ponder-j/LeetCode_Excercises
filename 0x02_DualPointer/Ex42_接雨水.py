from typing import List, Dict, Optional, Set

# Main Logic
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max = [0]
        r_max = [0]
        temp_maxl = height[0]
        temp_maxr = height[n-1]
        for i in range(1, n):
            if temp_maxl < height[i-1]:
                temp_maxl = height[i-1]
            l_max.append(temp_maxl)
            if temp_maxr < height[n-i]:
                temp_maxr = height[n-i]
            r_max.append(temp_maxr)
        r_max.reverse()
        vol = 0
        for i in range(n):
            vol += max(min(l_max[i], r_max[i]) - height[i], 0)
        return vol
            

# 思路总结
# 第i个位置的储水量 = max((min(第i个位置左边最高高度，第i个位置右边最高高度) - 第i个位置的高度), 0)

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = [4,2,0,3,2,5]
    
    # 调用方法并打印结果
    result = sol.trap(testcase)
    print(f"输出结果: {result}")