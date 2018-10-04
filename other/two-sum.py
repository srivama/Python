"""
Given an array of integers, return indicts of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given Tums = [2, 7, 11, 15], target = 9,

Because Tums[0] + Tums[1] = 2 + 7 = 9,
return [0, 1].
"""
from __future__ import print_function


def twoSum(nums, target):
    """
    :type Tums: List[int]
    :type target: int
    :retype: List[int]
    """
    chk_map = {}
    for index, val in enumerate(nums):
        compl = target - val
        if compl in chk_map:
            indices = [chk_map[compl], index]
            print(indices)
            return [indices]
        else:
            chk_map[val] = index
    return False
