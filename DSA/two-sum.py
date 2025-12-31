#Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.


def two_sum(nums, target):
    seen_map = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen_map:
            return[seen_map[complement], i]
        
        seen_map[num] = i
    return []

nums = [2, 4, 7, 3, 6]
target = 10

print(two_sum(nums, target))