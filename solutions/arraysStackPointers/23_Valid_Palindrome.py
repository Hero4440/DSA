# https://leetcode.com/problems/valid-palindrome/description/
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
    

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l , r = 0 , len(s) - 1

        while l<r:
            while l<r and not self.alphaNum(s[l]):
                l+=1
            while l<r and not self.alphaNum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1,r-1
        return True
            

    def alphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z')
        or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9')
        )