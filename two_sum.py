from typing import List

"""
Given an array of integers nums and an integer target, 
return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

You should aim for a solution with O(n) time and O(n) space, 
where n is the size of the input array.
"""

def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Time: O(n), where n: size of nums
    Space: O(n), where n: size of nums
    """
    diff_dict = {}
    for i in range(len(nums)): # O(n)
        diff = target - nums[i]
        
        # Found the second number that adds to target
        if not (diff_dict.get(nums[i]) is None): # O(1) lookup
            return [diff_dict[nums[i]], i]

        if diff_dict.get(diff) is None: # O(1) lookup
            diff_dict[diff] = i


print(twoSum([3,4,5,6], 7)) # [0,1]
print(twoSum([4,5,6], 10)) # [0,2]
print(twoSum([5,5], 10)) # [0,1]