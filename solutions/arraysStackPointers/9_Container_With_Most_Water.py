# https://leetcode.com/problems/container-with-most-water/
# 11. Container With Most Water
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            # Calculate the area of the current container
            current_area = (right - left) * min(height[left], height[right])
            max_water = max(max_water, current_area)

            # Move the smaller height pointer inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water