from typing import List, Dict, Optional, Set

# Main Logic
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        intervals.sort(key = lambda x: x[0])
        temp = intervals[0]
        for i in range(1, n):
            if temp[1] < intervals[i][0]:
                ans.append(temp)
                temp = intervals[i]
            else:
                temp[1] = max(temp[1], intervals[i][1])
        ans.append(temp)
        return ans

# 思路总结
# 首先想到按 start 对原数组进行排序，这样相邻两个区间只有这几种情况了 [start_i, end_i], [start_j, end_j]
# end_i < start_j 区间直接断开来
# end_i >= start_j:
#   end_i < end_j: 两个区间合并为一个 [start_i, end_j]
#   end_i >= end_j: 两个区间合并为一个 [start_i, end_i]
# 后面两种可以合并为一个结果：[start_i, max{end_i, end_j}]

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = [[1,3],[2,6],[8,10],[15,18]]
    
    # 调用方法并打印结果
    result = sol.merge(testcase)
    print(f"输出结果: {result}")