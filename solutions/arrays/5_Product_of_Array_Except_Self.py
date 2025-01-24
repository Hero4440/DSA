# # https://leetcode.com/problems/product-of-array-except-self/description/
# #  238. Product of Array Except Self
# # Solved
# # Medium
# # Topics
# # Companies
# # Hint
# # Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# # The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# # You must write an algorithm that runs in O(n) time and without using the division operation.


# Solution for “238. Product of Array Except Self”

# Approach 1: Prefix and Suffix Product Arrays (O(n) Time, O(n) Space)

# We can solve this by computing prefix and suffix products separately.

# Algorithm:
# 	1.	Compute Prefix Products:
# 	•	prefix[i] stores the product of all elements before index i.
# 	2.	Compute Suffix Products:
# 	•	suffix[i] stores the product of all elements after index i.
# 	3.	Compute Final Answer:
# 	•	answer[i] = prefix[i] * suffix[i].

# Code:

# class Solution:
#     def productExceptSelf(self, nums):
#         n = len(nums)
#         prefix = [1] * n
#         suffix = [1] * n
#         answer = [1] * n

#         # Compute prefix product
#         for i in range(1, n):
#             prefix[i] = prefix[i - 1] * nums[i - 1]

#         # Compute suffix product
#         for i in range(n - 2, -1, -1):
#             suffix[i] = suffix[i + 1] * nums[i + 1]

#         # Compute answer
#         for i in range(n):
#             answer[i] = prefix[i] * suffix[i]

#         return answer

# Complexity Analysis:
# 	•	Time Complexity: O(n) (Two passes to compute prefix/suffix, one to compute result)
# 	•	Space Complexity: O(n) (Separate prefix and suffix arrays)

# Approach 2: Optimized Space (O(n) Time, O(1) Extra Space)

# We can optimize space by using the answer array itself for storing prefix and suffix products.

# Algorithm:
# 	1.	Use answer[] to store prefix products initially.
# 	2.	Iterate backward to compute suffix products on the fly, updating answer[].

# Code:

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # Compute prefix product in answer array
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Compute suffix product on the fly and multiply with prefix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

# Complexity Analysis:
# 	•	Time Complexity: O(n) (Two passes: forward for prefix, backward for suffix)
# 	•	Space Complexity: O(1) (Only output array, no extra storage)

# Comparison of Approaches

# Approach	Time Complexity	Space Complexity	Notes
# Brute Force (O(n²))	O(n²)	O(1)	Nested loops (Too slow for large n)
# Prefix & Suffix (O(n))	O(n)	O(n)	Uses extra prefix and suffix arrays
# Optimized Space (O(n))	O(n)	O(1)	Uses only answer[] for final computation

# Final Thoughts

# ✅ Use the optimized O(1) space approach (last solution).
# ✅ It efficiently computes the result using prefix and suffix multiplications.
         
