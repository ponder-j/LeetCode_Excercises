from typing import List, Dict, Optional, Set

# Main Logic
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            target = -nums[i]
            while left < right:
                sum2 = nums[left] + nums[right]
                if sum2 == target:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while (left < right and nums[left] == nums[left-1]):
                        left += 1
                    while (left < right and nums[right] == nums[right+1]):
                        right -= 1
                elif sum2 < target:
                    left += 1
                elif sum2 > target:
                    right -= 1
        return ans

# 思路总结
# 容易想到固定一个数，再去搜另外两个数，这时候由于另外两个数之和已经固定，所以可以用双指针对一个有序数组进行搜索，从而降低时间复杂度

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
    
    # 调用方法并打印结果
    result = sol.threeSum(testcase)
    print(f"输出结果: {result}")