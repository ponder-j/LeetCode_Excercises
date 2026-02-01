from typing import List, Dict, Optional, Set

# Main Logic
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        ans = []
        p_dict = {}
        n = len(s)
        p_len = len(p)
        for i in range(p_len):
            if p[i] not in p_dict:
                p_dict[p[i]] = 1
            else:
                p_dict[p[i]] += 1
        
        p_dict_backup = p_dict.copy()

        while l < n:
            while s[l] not in p_dict:
                l += 1
                if l == n:
                    return ans
            r = l
            # 确保了刚进入时必定有 s[l(=r)] in p_dict
            while r < n:
                if s[r] in p_dict: # 如果 s[r] 都不在字母集合中了，可以直接让 l = r+1 进行下一轮窗口滑动
                    if p_dict[s[r]] != 0: # 字母还有剩余; 如果没有剩余了就应该移动 l 了
                        p_dict[s[r]] -= 1
                        r += 1
                        if r - l == p_len:
                            ans.append(l)
                    else:
                        p_dict[s[l]] += 1
                        l += 1
                else:
                    l = r + 1
                    r = l
                    p_dict = p_dict_backup.copy()
                    break
        return ans
                    
                    
                
                    
        
# 思路总结

# Instantiation
if __name__ == '__main__':
    # 实例化 Solution 类
    sol = Solution()
    
    # 构造测试用例
    s = "acdcaeccde"
    p = "c"
    
    # 调用方法并打印结果
    result = sol.findAnagrams(s, p)
    print(f"输出结果: {result}")