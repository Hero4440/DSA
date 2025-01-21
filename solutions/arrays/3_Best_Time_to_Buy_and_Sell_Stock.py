# # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# SOLUTION:
# One Pass Approach (O(n) Time Complexity)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mIn = float("inf")
        mAx = 0 
        for price in prices:
            mIn = min(mIn,price)
            mAx = max(mAx, price - mIn)
        return mAx

# Kadane’s Algorithm (O(n) Time Complexity)
# class Solution:
    # def maxProfit(self, prices):
    #     maxProfit = 0
    #     currProfit = 0  # Tracks the ongoing profit streak

    #     for i in range(1, len(prices)):  # Start from day 1 (index 1)
    #         currProfit += prices[i] - prices[i - 1]  # Compute daily price change
    #         currProfit = max(0, currProfit)  # Reset to 0 if profit streak goes negative
    #         maxProfit = max(maxProfit, currProfit)  # Track max profit

    #     return maxProfit

# Brute Force Approach (O(n^2) Time Complexity)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maxProf = 0
#         for price in range(len(prices)):
#             bought = prices[price]
#             for x in range(price +1 ,len(prices)):
#                 sell = prices[x]
#                 if maxProf < sell - bought:
#                     maxProf = sell - bought
#         return maxProf


        