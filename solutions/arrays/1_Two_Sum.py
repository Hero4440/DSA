# https://leetcode.com/problems/two-sum/description/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for x in range(len(nums)):
            comp = target - nums[x]
            if comp in hashmap:
                return [hashmap[comp] , x]
            hashmap[nums[x]] = x
        return []

# Time complexity: O(n)
# Space complexity: O(n)

#  brute force solution
# def twoSum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i + 1, n):  # Ensures no duplicate use of elements
#             if nums[i] + nums[j] == target:
#                 return [i, j]