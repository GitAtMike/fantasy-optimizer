# Given a list of numbers sorted in ascending order, find two numbers that add up to a given target. Return their values (or indices - your choice)
# Example: nums = [2, 7, 11, 15], target = 9 -> return 2 and 7 (since 2 + 7 = 9).
# Do it without a nested loop.

def sumToTarget(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] == target:
            return nums[left], nums[right]

        elif nums[left] + nums[right] > target:
            right -= 1

        else:
            left += 1

print(sumToTarget([2, 7, 11, 15], 9))