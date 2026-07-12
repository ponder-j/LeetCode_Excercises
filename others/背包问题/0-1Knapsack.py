from typing import List

# 每个物品只有一件，要么选（1），要么不选（0）
def zero_one_knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    """
    weights: 物品重量
    values: 物品价值
    capacity: 背包最大容量
    """
    n = len(weights)
    # dp[j] 表示容量为 j 的背包能装的最大价值
    dp = [0] * (capacity + 1)
    
    # 迭代 n 轮
    for i in range(n):
        # 枚举 j
        for j in range(capacity, weights[i]-1, -1):
            # 对于物品 i，取了好还是不取好
            dp[j] = max(dp[j], dp[j-weights[i]] + values[i])
            
    return dp[capacity]