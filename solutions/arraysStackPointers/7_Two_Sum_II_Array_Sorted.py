# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# 167. Two Sum II - Input Array Is Sorted
# Solved
# Medium
# Topics
# Companies
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

# two-pointer approach time complexity is O(n) and space complexity is O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l<r:
            if target > numbers[l] +  numbers[r]:
                l += 1
            elif target < numbers[l] +  numbers[r]:
                r -=1
            else:
                return [l+1,r+1]
            
# brute force approach time complexity is O(n^2) and space complexity is O(1)
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)):
#             for j in range(i+1,len(numbers)):
#                 if numbers[i] + numbers[j] > target:
#                     continue
#                 if numbers[i] + numbers[j] == target:
#                     return [i+1,j+1]
#         return []