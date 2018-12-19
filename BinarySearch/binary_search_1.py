def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
    	mid = (l + r)//2
    	if nums[mid] == target:
    		return mid
    	elif nums[mid] < target:
    		r = mid + 1
    	elif nums[mid] > target:
    		l = mid -1
    return -1


'''
This is the most basic and elementary form of Binary Search.
It is the standard Binary Search Template that most high schools
or universities use when they first teach students computer science.
Template 1 is used to search for an element or condition which can be
determined by accessing a single index in the array.

Key Attributes:

Most basic and elementary form of Binary Search
Search Condition can be determined without comparing to the element's neighbors
(or use specific elements around it)
No post-processing required because at each step, you are checking to see if
the element has been found. If you reach the end, then you know the element is not found
 

Distinguishing Syntax:

Initial Condition: left = 0, right = length-1
Termination: left > right
Searching Left: right = mid-1
Searching Right: left = mid+1
'''