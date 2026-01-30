from typing import List, Dict, Optional, Set

# Main Logic
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_vol = area(height, left, right)
        while left < right:
            if height[left] >= height[right]: # 若 左指针数 >= 右指针数，则短板为右指针数，假设右指针数仍有可能为右边界，则滑动左指针，由于滑动过程中间距在缩短而高度不可能增长（因为短板被卡死在右指针数），所以不可能得到比当前还大的容量，假设不成立，进而右边界可以进行更新
                right -= 1
            elif height[left] < height[right]: # 若 左指针数 < 右指针数，同理左边界可以进行更新
                left += 1
            max_vol = max(area(height, left, right), max_vol)
        return max_vol
    
def area(h, x, y):
    return (y - x) * min(h[x], h[y])
        

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = [1,8,6,2,5,4,8,3,7] 
    
    # 调用方法并打印结果
    result = sol.maxArea(testcase)
    print(f"输出结果: {result}")