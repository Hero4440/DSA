# https://leetcode.com/problems/encode-and-decode-strings/description/
# https://neetcode.io/problems/string-encode-and-decode
# Encode and Decode Strings
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res
            
        return res
    def decode(self, s: str) -> List[str]: 
        print("res",s)
        res, i = [] , 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1
            length = int(s[i:j])
            res.append(s[j+1: j+ 1 + length])
            i = j + 1 + length
        return res