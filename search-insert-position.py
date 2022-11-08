"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while high >= low:

        mid = (low + high) // 2

        if nums[mid] == target:
            break
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return mid
    else:
        return mid + 1


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    assert searchInsert(nums=nums, target=target) == 2
    nums = [1, 3, 5, 6]
    target = 2
    assert searchInsert(nums=nums, target=target) == 1
    nums = [1, 3, 5, 6]
    target = 7
    assert searchInsert(nums=nums, target=target) == 4
    nums = [1, 3, 5, 6]
    target = 0
    assert searchInsert(nums=nums, target=target) == 0
    nums = [1, 3]
    target = 2
    assert searchInsert(nums=nums, target=target) == 1
