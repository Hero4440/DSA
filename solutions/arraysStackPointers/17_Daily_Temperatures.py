# https://leetcode.com/problems/daily-temperatures/description/
# 739. Daily Temperatures
# Medium
# Topics
# Companies
# Hint
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, value in enumerate(temperatures):
            while stack and value > stack [-1][0]:
                stackValue , stackInd = stack.pop()
                res [stackInd] = index - stackInd
            stack.append([value, index])

        return res
  # Time Complexity: O(n) Space Complexity: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        right = 1
        print(res, "result")
        for index, value in enumerate(temperatures):
            for r in range(1, len(temperatures)):
                if temperatures [index] < temperatures[r]:
                    res[index] = r - index
                    break
        return res
# Time Complexity: O(n^2) Space Complexity: O(n)

