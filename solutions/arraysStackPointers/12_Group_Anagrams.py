# https://leetcode.com/problems/group-anagrams/description/

# 49. Group Anagrams
# Given an array of strings strs, group the 
# anagrams
#  together. You can return the answer in any order.





# sorting approach time complexity O(n * k log k) space complexity O(n)
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
#         for s in strs:
#             sortedString = ''.join(sorted(s))
#             res[sortedString].append(s)
#         print( list(res.values()))
#         return list(res.values())

# hash map approach time complexity O(n * k) space complexity O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())