# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums_set = list(set(nums))
#         n = len(nums_set)
#         longest = 0
#         hashdic = {}
#         for num in nums_set:
#             hashdic[num] = 1
#         for num in nums_set:
#             x = num
#             if x-1 not in hashdic:
#                 temp = 1
#                 while True:
#                     if x + 1 in hashdic:
#                         temp += 1
#                         x += 1
#                     else:
#                         break
#                 if temp > longest:
#                     longest = temp
#         return longest

# 超时了
# def longestConsecutive(nums):
#     nums_set = list(set(nums))
#     n = len(nums_set)
#     longest = 0
#     for i in range(n):
#         if nums_set[i]-1 not in nums_set:
#             x = nums_set[i]
#             temp = 1
#             while True:
#                 if x + 1 in nums_set:
#                     temp += 1
#                     x += 1
#                 else:
#                     break
#             if temp > longest:
#                 longest = temp
#     return longest

def longestConsecutive(nums):
    nums_set = list(set(nums))
    n = len(nums_set)
    longest = 0
    hashdic = {}
    for num in nums_set:
        hashdic[num] = 1
    for num in nums_set:
        x = num
        if x-1 not in hashdic:
            temp = 1
            while True:
                if x + 1 in hashdic:
                    temp += 1
                    x += 1
                else:
                    break
            if temp > longest:
                longest = temp
    return longest

print(longestConsecutive([1,0,1,2]))