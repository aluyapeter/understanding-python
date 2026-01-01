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

# Two sum II
# Input: nums = [2, 7, 11, 15], target = 9 (Note: It is sorted).Constraint: You cannot use a Hash Map. A Hash Map uses $O(n)$ memory. I want $O(1)$ memory (no extra data structures).

def two_sum_ii(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l < r:
        sum = numbers[l] + numbers[r]

        if sum > target:
            r -= 1
        elif sum < target:
            l += 1
        else:
            return [l, r]
    return []
    
nums = [2, 7, 11, 15]
target = 9
print(two_sum_ii(nums, target))