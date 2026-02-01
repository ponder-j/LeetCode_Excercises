from typing import List, Dict, Optional, Set

# Main Logic
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = []
        n = len(nums)
        pre_dict = {}
        pre_dict[0] = 1
        cnt = 0
        for i in range(n):
            if i == 0:
                prei = nums[i]
                pre.append(nums[i])
            else:
                prei = pre[i-1] + nums[i]
                pre.append(prei)
            
            check = pre[i] - k
            if check in pre_dict:
                cnt += pre_dict[check]
            
            if prei not in pre_dict:
                pre_dict[prei] = 1
            else:
                pre_dict[prei] += 1
            
        return cnt
                    

# 思路总结
# 一开始想用双指针/滑动窗口，发现 nums 里的整数可能是负的，这样就不能这么做了
# 重点在想到先确定结尾，按结尾枚举而不是按开头枚举
# sum(j, i) == k -> sum(0, i) - sum(0, j) == k -> sum(0, j) == sum(0, i) - k ，对于一个 i，把前缀和存哈希表就可以实现 O(1) 复杂度找到有几个 j 符合要求

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    nums = [1,1,1]
    k = 2
    
    # 调用方法并打印结果
    result = sol.subarraySum(nums, k)
    print(f"输出结果: {result}")