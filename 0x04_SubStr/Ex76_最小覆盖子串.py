from typing import List, Dict, Optional, Set

# Main Logic
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        target_dict = {}
        for c in t:
            if c not in target_dict:
                target_dict[c] = 1
            else:
                target_dict[c] += 1
        cur_dict = dict.fromkeys(target_dict, 0)
        shortest_len = n + 1
        anslr = (0, -1)
        
        l = r = 0
        while l <= r and r < n:
            if s[r] in target_dict:
                cur_dict[s[r]] += 1
                if self.checkSubstr(cur_dict, target_dict):
                    ans_len = r - l + 1
                    if ans_len < shortest_len:
                        anslr = (l, r)
                        shortest_len = ans_len
                    # 通过移动 l 来缩小窗口
                    while self.checkSubstr(cur_dict, target_dict):
                        ans_len = r - l + 1
                        if ans_len < shortest_len:
                            anslr = (l, r)
                            shortest_len = ans_len
                        if s[l] in cur_dict:
                            cur_dict[s[l]] -= 1
                        l += 1
                    # 通过移动 r 来增大窗口
                    r += 1
                else:
                    r += 1
            else:
                r += 1
                                            
        return s[anslr[0]: anslr[1]+1]
    def checkSubstr(self, cur: dict, target: dict) -> bool:
        for idx in cur:
            if cur[idx] < target[idx]:
                return False
        return True
        
# 思路总结

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    s = "a"
    t = "a"
    
    # 调用方法并打印结果
    result = sol.minWindow(s, t)
    print(f"输出结果: {result}")