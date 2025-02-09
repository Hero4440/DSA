# https://leetcode.com/problems/longest-consecutive-sequence/description/
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
 
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# 1. Brute Force Approach Time complexity: O(n^2) Space complexity: O(n)
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         res = 0
#         store = set(nums)

#         for num in nums:
#             streak, curr = 0, num
#             while curr in store:
#                 streak += 1
#                 curr += 1
#             res = max(res, streak)
#         return res

# 2. Sorting Approach Time complexity: O(nlogn) Space complexity: O(1)
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         res = 0
#         nums.sort()
        
#         curr, streak = nums[0], 0
#         i = 0
#         while i < len(nums):
#             if curr != nums[i]:
#                 curr = nums[i]
#                 streak = 0
#             while i < len(nums) and nums[i] == curr:
#                 i += 1
#             streak += 1
#             curr += 1
#             res = max(res, streak)
#         return res
# 3. Hash Set Time complexity: O(n) Space complexity: O(n)
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         numSet = set(nums)
#         longest = 0
#         for num in numSet:
#             if (num - 1) not in numSet:
#                 length = 1
#                 while (num + length) in numSet:
#                     length += 1
#                 longest = max(length, longest)
#         return longest

# 4. Hash Map Time complexity: O(n) Space complexity: O(n)
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         mp = defaultdict(int)
#         res = 0

#         for num in nums:
#             if not mp[num]:
#                 mp[num] = mp[num - 1] + mp[num + 1] + 1
#                 mp[num - mp[num - 1]] = mp[num]
#                 mp[num + mp[num + 1]] = mp[num]
#                 res = max(res, mp[num])
#         return res