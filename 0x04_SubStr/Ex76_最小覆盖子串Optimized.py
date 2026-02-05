from typing import List
import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1. 处理边界条件
        if not t or not s:
            return ""
        
        # 2. 统计 t 中需要的字符频率
        target_counts = collections.Counter(t)
        required_unique_chars = len(target_counts) # t 中有多少个独特的字符需要满足
        
        # 3. 初始化滑动窗口的状态
        l, r = 0, 0
        formed = 0  # 当前窗口中，有多少个字符已经满足了 t 中的数量要求
        window_counts = collections.defaultdict(int)
        
        # 记录结果 (窗口长度, 左边界, 右边界)
        # 初始化为一个不可能的长度 float('inf')
        ans = float('inf'), None, None
        
        # 4. 开始滑动窗口
        while r < len(s):
            # --- 进窗口 ---
            char = s[r]
            window_counts[char] += 1 # 不管是不是需要的字符，全都可以加进来，反正最后 char in target_counts 还要重新判断过
            
            # 如果当前字符是 t 需要的，且数量达到了要求，formed 加 1
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1
            
            # --- 出窗口（收缩） ---
            # 只要当前窗口满足了所有独特字符的要求 (formed == required_unique_chars)
            # 我们就尝试收缩左边界 l，试图找到更小的窗口
            while l <= r and formed == required_unique_chars:
                char = s[l]
                
                # 更新最小窗口记录
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # 移除左边的字符
                window_counts[char] -= 1
                # 关键点：如果移除后，该字符数量小于了目标数量，则 formed 减 1
                # 这意味着窗口不再合法，循环将终止，开始继续移动右指针
                if char in target_counts and window_counts[char] < target_counts[char]:
                    formed -= 1
                
                l += 1    
            
            # 继续移动右指针
            r += 1    
        
        return "" if ans[0] == float('inf') else s[ans[1] : ans[2] + 1]

# 思路总结
# 滑动窗口标准写法：外循环动 r，内循环动 l
# 用 collections.defaultdict() 避免哈希表手动写分支初始化
# 前一个方法每次判断是否符合要求都要经历一遍 O(len(t)) 的操作太蠢了，这里用 formed 记录达标符号的个数，优化到 O(1)

# 实例化测试
if __name__ == '__main__':
    sol = Solution()
    print(f"输出结果: {sol.minWindow('ADOBECODEBANC', 'ABC')}")