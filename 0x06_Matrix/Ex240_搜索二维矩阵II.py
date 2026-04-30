from typing import List, Dict, Optional, Set

# Main Logic
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag = False
        bigger = False
        n = len(matrix)
        l_slope, r_slope = 0, n-1
        while l_slope < r_slope:
            mid = (l_slope + r_slope) // 2
            print(mid)
            if matrix[mid][mid] == target:
                flag = True
                return flag
            elif matrix[mid][mid] < target:
                l_slope = mid + 1
                bigger = True
            else:
                r_slope = mid - 1
                bigger = False
        
        b = l_slope
        if bigger == False:
            b += 1
        
        return flag

# 思路总结

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 20
    # 调用方法并打印结果
    result = sol.searchMatrix(testcase, target)
    print(f"输出结果: {result}")