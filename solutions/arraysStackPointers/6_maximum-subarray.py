# # # https://leetcode.com/problems/maximum-subarray/description/

# # 53. Maximum Subarray
# # Solved
# # Medium
# # Topics
# # Companies
# # Given an integer array nums, find the 
# # subarray
# #  with the largest sum, and return its sum.

 

# # Example 1:

# # Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# # Output: 6
# # Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# LeetCode 53: Maximum Subarray

# 🔹 Problem Statement

# Given an integer array nums, find the contiguous subarray (containing at least one number) that has the largest sum and return its sum.

# 🔹 Example

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum = 6.

# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The only subarray is [1], so the max sum = 1.

# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum = 23.

# 🔹 Solution Approaches

# 1️⃣ Brute Force Approach (O(n²))
# 	•	Check all possible subarrays and find the max sum.
# 	•	Time Complexity: O(n²), because we check every possible subarray.
# 	•	Space Complexity: O(1), as we use only a few variables.

# Python Code:

# def maxSubArray(nums):
#     max_sum = float('-inf')
#     for i in range(len(nums)):
#         curr_sum = 0
#         for j in range(i, len(nums)):
#             curr_sum += nums[j]
#             max_sum = max(max_sum, curr_sum)
#     return max_sum

# 2️⃣ Kadane’s Algorithm (O(n)) — Optimal Approach
# 	•	The idea is to iterate through the array while maintaining a running sum (current_sum).
# 	•	If current_sum becomes negative, reset it to 0 and start fresh.
# 	•	Time Complexity: O(n), as we traverse the array once.
# 	•	Space Complexity: O(1), since we use only a few extra variables.

# Python Code:

def maxSubArray(nums):
    max_sum = nums[0]  # Initialize with the first element
    current_sum = 0

    for num in nums:
        if current_sum < 0:
            current_sum = 0  # Reset when sum becomes negative
        current_sum += num
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# 3️⃣ Divide & Conquer Approach (O(n log n))
# 	•	Divide: Split the array into two halves.
# 	•	Conquer: Recursively find the maximum subarray sum in both halves.
# 	•	Combine: Find the max crossing subarray that spans both halves.
# 	•	Time Complexity: O(n log n), since each recursion divides the array in half.
# 	•	Space Complexity: O(log n), due to recursive function calls.

# Python Code:

# def maxSubArray(nums):
#     def divide_and_conquer(left, right):
#         if left == right:
#             return nums[left]

#         mid = (left + right) // 2
#         left_sum = divide_and_conquer(left, mid)
#         right_sum = divide_and_conquer(mid + 1, right)
#         cross_sum = max_crossing_sum(nums, left, mid, right)

#         return max(left_sum, right_sum, cross_sum)

#     def max_crossing_sum(nums, left, mid, right):
#         left_max = float('-inf')
#         curr_sum = 0
#         for i in range(mid, left - 1, -1):
#             curr_sum += nums[i]
#             left_max = max(left_max, curr_sum)

#         right_max = float('-inf')
#         curr_sum = 0
#         for i in range(mid + 1, right + 1):
#             curr_sum += nums[i]
#             right_max = max(right_max, curr_sum)

#         return left_max + right_max

#     return divide_and_conquer(0, len(nums) - 1)

# 🔹 Summary of Approaches

# Approach	Time Complexity	Space Complexity	Notes
# Brute Force	O(n²)	O(1)	Tries all subarrays
# Kadane’s Algorithm	O(n)	O(1)	Best approach
# Divide & Conquer	O(n log n)	O(log n)	Uses recursion
