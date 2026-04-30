from typing import List, Dict, Optional, Set

# Main Logic
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lin = len(matrix)
        col = len(matrix[0])
        pos_x, pos_y = 0, col-1
        while pos_x <= lin-1 and pos_y >= 0:
            if matrix[pos_x][pos_y] < target:
                pos_x += 1
            elif matrix[pos_x][pos_y] > target:
                pos_y -= 1
            else:
                return True
        
        return False

# 思路总结
# 从右上角开始搜索，它同时是一列的最小值和一行的最大值，因此
# target 比当前位置大：这一行都不用看了，肯定都比 target 小
# target 比当前位置小：这一列都不用看了，肯定都比 target 大
# 因此每次比较都能砍掉一行或一列，效率高，时间复杂度 O(m+n)

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 15
    # 调用方法并打印结果
    result = sol.searchMatrix(testcase, target)
    print(f"输出结果: {result}")
    for i in testcase:
        for j in i:
            result = sol.searchMatrix(testcase, j)
            print(f"search:{j}, 输出结果: {result}")