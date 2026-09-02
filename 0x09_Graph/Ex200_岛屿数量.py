from typing import List, Dict, Optional, Set

# Main Logic
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

# 思路总结

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = [
        ['1','1','1','1','0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','0','0','0']
    ]
    
    # 调用方法并打印结果
    result = sol.numIslands(testcase)
    print(f"输出结果: {result}")