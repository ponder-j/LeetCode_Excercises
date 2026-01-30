from typing import List, Dict, Optional, Set

# Main Logic
class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0
        n = len(height)
        stack = []
        stack.append(0)
        i = 1
        while i < n:
            if height[i] < height[stack[-1]]:
                stack.append(i)
                i += 1
                continue
            while height[i] >= height[stack[-1]]:
                cur = stack.pop()
                if stack != []:
                    vol += (min(height[stack[-1]], height[i]) - height[cur]) * (i - stack[-1] - 1)
                else:
                    stack.append(i)
                    i += 1
                    break
            
        return vol
            

# 思路总结
# 第i个位置的储水量 = max((min(第i个位置左边最高高度，第i个位置右边最高高度) - 第i个位置的高度), 0)
# 单调栈解法：维护一个递减的单调栈，遇到一个高的就弹出栈顶元素，结算凹陷部分容量，同时相当于把这个凹陷“填平了”

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = [4,2,0,3,2,5]
    
    # 调用方法并打印结果
    result = sol.trap(testcase)
    print(f"输出结果: {result}")