# https://leetcode.com/problems/house-robber/description/
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        oneBack = nums[0]
        twoBack = 0
        for i in range(1,len(nums)):
            #choose whether to rob the current house or not
            temp = oneBack
            oneBack = max(nums[i]+twoBack,oneBack)
            twoBack= temp
        return oneBack
