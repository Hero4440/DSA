# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Sliding Window timne complexity O(n) space complexity O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        charSet = set()
        res = 0 
        for i in range(len(s)):
            while (s[i] in charSet):
                charSet.remove(s[left])
                left+=1
            charSet.add(s[i])
            res = max(res, i - left +1)
        return res

# Brute Force time complexity O(n^3) space complexity O(n)
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         res = 0
#         for i in range(len(s)):
#             charSet = set()
#             for j in range(i, len(s)):
#                 if s[j] in charSet:
#                     break
#                 charSet.add(s[j])
#             res = max(res, len(charSet))
#         return res