# https://leetcode.com/problems/top-k-frequent-elements/

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Input: nums = [1], k = 1
# Output: [1]
 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        feq = [[] for i in range(len(nums)+ 1)]
        for i in nums:
            count[i] = 1 + count.get(i,0)
        for i , cnt in count.items():
            feq[cnt].append(i)

        res = []
        for i in range(len(feq)-1, 0,-1):
            for num in feq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                