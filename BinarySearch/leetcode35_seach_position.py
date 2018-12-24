# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:

# Input: [1,3,5,6], 5
# Output: 2
# Example 2:

# Input: [1,3,5,6], 2
# Output: 1
# Example 3:

# Input: [1,3,5,6], 7
# Output: 4
# Example 4:

# Input: [1,3,5,6], 0
# Output: 0

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        m = 0
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        
        if l >= len(nums):
            return len(nums)
        if nums[l] < target:
            return l+1
        else:
            return l
        # In this solution, l ends up being r+1, which means it can be len(nums) + 1.

    def searchInsertAlternativeSol(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = 0
        r = len(nums)-1
        m = 0
        while l < r:
            mid = (l+r)//2
            m = mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
#         Note that after the while loop above, l can be up to len(nums)-1.
#         If target is larger then the last element of nums, we return len(nums), 
#         which is l + 1, and l can be up to len(nums) - 1.
        
#         Out side the while loop, nums[l] is likely to be target. 

        if nums[l] < target:
            return l + 1
        return l
