# question link: https://leetcode.com/problems/find-the-duplicate-number/


class Solution:
    def findDuplicate(self, nums) -> int:
        seen = set()
        for ele in nums:
            if ele in seen:
                return ele
            seen.add(ele)
