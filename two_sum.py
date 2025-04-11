from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    diff_dict = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        
        if not (diff_dict.get(nums[i]) is None):
            return [diff_dict[nums[i]], i]

        if diff_dict.get(diff) is None:
            diff_dict[diff] = i


print(twoSum([3,4,5,6], 7))
print(twoSum([4,5,6], 10))