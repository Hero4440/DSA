# https://leetcode.com/problems/valid-anagram/description/


# Approach 1: Sorting (O(n log n) Time, O(1) Space)
# 	•	Sort both strings and compare them.
# 	•	If s and t have the same sorted order, they are anagrams.

# Code:

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

# Complexity Analysis:
# 	•	Time Complexity: O(n log n) (Sorting takes O(n log n))
# 	•	Space Complexity: O(1) (Sorting is in-place, but Python creates new sorted strings)

# Approach 2: HashMap (Character Count) (O(n) Time, O(1) Space)
# 	•	Count occurrences of each character in s and t.
# 	•	If the character counts match, the strings are anagrams.

# Code:

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Complexity Analysis:
# 	•	Time Complexity: O(n) (Building and comparing hashmaps)
# 	•	Space Complexity: O(1) (Only 26 lowercase English letters, fixed hashmap size)

# Approach 3: Optimized HashMap (Without Counter)
# 	•	Use an array of size 26 instead of a dictionary.

# Code:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = [0] * 26

        for char in s:
            char_count[ord(char) - ord('a')] += 1
        for char in t:
            char_count[ord(char) - ord('a')] -= 1

        return all(count == 0 for count in char_count)

# Complexity Analysis:
# 	•	Time Complexity: O(n)
# 	•	Space Complexity: O(1), since we use only 26 elements.

# Approach 4: Unicode Support
# 	•	Instead of a fixed array, use defaultdict(int) for any character set.

# Code:

# from collections import defaultdict

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         char_count = defaultdict(int)

#         for char in s:
#             char_count[char] += 1
#         for char in t:
#             char_count[char] -= 1
#             if char_count[char] < 0:
#                 return False

#         return True

# Complexity Analysis:
# 	•	Time Complexity: O(n)
# 	•	Space Complexity: O(1) for ASCII, O(k) for Unicode (k = unique characters).

# Comparison of Approaches

# Approach	Time Complexity	Space Complexity	Notes
# Sorting (O(n log n))	O(n log n)	O(1)	Simple but slow
# HashMap (Counter)	O(n)	O(1)	Fast and clean
# Optimized Array (O(n))	O(n)	O(1)	Best for lowercase letters
# Unicode (O(n))	O(n)	O(k)	Best for any character set

# Final Thoughts

# ✅ Use Counter or array-based HashMap for O(n) time.
# ✅ Use defaultdict(int) for Unicode support.
# ✅ Sorting approach is not optimal (O(n log n)).

# Would you like a test case breakdown? 🚀