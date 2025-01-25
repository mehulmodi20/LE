from typing import List


def search(nums: List[int], target: int) -> int:
    if len(nums) == 1:
        if target == nums[0]:
            return 0
        else:
            return -1
    midPoint = len(nums) // 2
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        if nums[midPoint] == target:
            return midPoint
        # print(midPoint)
        if target > nums[midPoint]:
            left = midPoint + 1
        else:
            right = midPoint - 1
        midPoint = (left + right) // 2
    return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
print(search([-1, 0, 3, 5, 9, 12], 13))
print(search([-1, 0, 5], 0))
