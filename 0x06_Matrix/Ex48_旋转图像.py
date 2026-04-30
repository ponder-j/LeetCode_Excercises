from typing import List, Dict, Optional, Set

# Main Logic
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 顺时针旋转 90 度 等价于 上下翻转+转置
        n = len(matrix)
        for i in range(n//2):
            for j in range(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]
        
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# 思路总结

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = [[1,2,3],[4,5,6],[7,8,9]]
    
    # 调用方法并打印结果
    result = sol.rotate(testcase)
    # print(f"输出结果: {testcase}")
    for l in testcase:
        print(l)