# https://leetcode.com/problems/contains-duplicate/description/

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# SOLUTION:

# Using a Hash Set (Optimal Solution) O(n) Time Complexity)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)
        return False

# Hash Map (Dictionary) Approach (O(n) Time Complexity)
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hashmap = {}
#         for num in nums:
#             if num in hashmap:
#                 return True
#             hashmap[num] = 1
#         return False

# Sorting + Checking Adjacent Elements O(n log n) Time Complexity
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for x in range( len(nums) - 1):
#             if nums[x] == nums[x+1]:
#                 return True
#         return False
        