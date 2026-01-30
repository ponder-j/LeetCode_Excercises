class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        min_max = 0
        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(nums, mid, k) == False:
                left = mid + 1
            else:
                min_max = mid
                right = mid - 1
        return min_max

# def splitArray(nums, k):
#     min_max = 0
#     left = max(nums)
#     right = sum(nums)
#     while left <= right:
#         mid = (left + right) // 2
#         if check(nums, mid, k) == False:
#             left = mid + 1
#         else:
#             min_max = mid
#             right = mid - 1
#     return min_max

def check(nums, max, k):
    partial_sum = 0
    cnt = 1
    for i in range(len(nums)):
        if partial_sum + nums[i] <= max:
            partial_sum += nums[i]
        else:
            cnt += 1
            partial_sum = nums[i]
    return (cnt <= k)

print(splitArray([7,2,5,10,8], 2))