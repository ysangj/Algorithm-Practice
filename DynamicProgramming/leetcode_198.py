# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.


# let dp[i] be the profit by the time the robber gets to i_th house.
# For each house he visits, the robber has to decide between following two choices to maximize the profit.

# 1. The robber does not rob the i-1_th house and robs ith house. --> dp[i-2] + nums[i]

# 2. The robber robs i-1_th house and leave i_th house alone. --> dp[i-1]

# Thus, dp[i] = max(dp[i-2] + nums[i], dp[i-1])
# And the base case is, dp[0] = nums[0], dp[1] = max(nums[0], nums[1]) because if there are only 2 houses, robber can only rob the
# one with the higher money.

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

		if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp = [0] * len(nums)
        
        #base case
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        #tabulization
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[-1]


