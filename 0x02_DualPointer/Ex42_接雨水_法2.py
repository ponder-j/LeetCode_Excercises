from typing import List, Dict, Optional, Set

# Main Logic
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        temp_maxl = height[0]
        temp_maxr = height[n-1]
        vol = 0
        while l < r:
            if height[l] < height[r]:
                # 已经找到一根右边比自己高的柱子了，说明能接多少水全看左侧最高有多少（当然要是左侧最高都没自己高那就接不了水）
                vol += max(temp_maxl - height[l], 0)
                l += 1
                temp_maxl = max(temp_maxl, height[l])
            else:
                # 已经找到一根左边比自己高的柱子了，说明能接多少水全看右侧最高有多少（当然要是右侧最高都没自己高那就接不了水）
                vol += max(temp_maxr - height[r], 0)
                r -= 1
                temp_maxr = max(temp_maxr, height[r])
            
        return vol
            

# 思路总结
# 第i个位置的储水量 = max((min(第i个位置左边最高高度，第i个位置右边最高高度) - 第i个位置的高度), 0)
# 双指针解法

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = [0,1,0,2,1,0,1,3,2,1,2,1]
    
    # 调用方法并打印结果
    result = sol.trap(testcase)
    print(f"输出结果: {result}")