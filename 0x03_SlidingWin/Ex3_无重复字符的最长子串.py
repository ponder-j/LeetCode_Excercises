from typing import List, Dict, Optional, Set

# Main Logic
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        cnt = 0
        max_cnt = 0
        cur_set = set()
        n = len(s)
        if n == 0 or n == 1:
            return n
        while l < n:
            while r < n:
                if s[r] not in cur_set:
                    cur_set.add(s[r])
                    cnt += 1
                    r += 1
                else:
                    break
            cur_set.remove(s[l])
            max_cnt = max(max_cnt, cnt)
            cnt -= 1
            l += 1
        return max_cnt

# 思路总结
# 滑动窗口，并且需要用到哈希表结构，用于快速判断是否存在重复元素
# 为什么可以“滑动”，也即为什么 r 指针永远向右移动而不需要回头判断？因为 r 能走到这一步说明之前都没有重复的，所以不需要回头

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    testcase = "au"
    
    # 调用方法并打印结果
    result = sol.lengthOfLongestSubstring(testcase)
    print(f"输出结果: {result}")