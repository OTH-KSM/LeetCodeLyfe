#!/usr/bin/env python3


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    ret = [0,0]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                ret[0] = i
                ret[1] = j
                return(ret)

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))