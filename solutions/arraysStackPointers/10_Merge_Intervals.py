# https://leetcode.com/problems/merge-intervals/

# 56. Merge Intervals
# Medium
# Topics
# Companies
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0] )
        print("list",intervals)
        output = [intervals[0]]
        for start,  end in intervals[1:]:
            lastEnd = output[-1][1]
            if lastEnd >= start:
                output[-1][1] = max(end, lastEnd)
            else:
                output.append([start,end])
        return output


        