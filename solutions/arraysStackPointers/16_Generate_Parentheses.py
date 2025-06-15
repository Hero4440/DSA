# https://neetcode.io/problems/generate-parentheses
# 22. Generate Parentheses
# You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

# Example 1:

# Input: n = 1

# Output: ["()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open < n
        # only add a closing parenthesis if closed < open
        # valid IIF open == closed == n
        
        stack = []
        res = []
        def recursive(openN , CloseN):
            if openN == CloseN == n:
                res.append(''.join(stack))
                return
            if openN < n:
                stack.append('(')
                recursive(openN + 1, CloseN)
                stack.pop()
            if CloseN < openN:
                stack.append(')')
                recursive(openN, CloseN + 1)
                stack.pop()
        recursive(0, 0)
        return res
# Time Complexity: O(4^n / sqrt(n)) Space Complexity: O(n)'