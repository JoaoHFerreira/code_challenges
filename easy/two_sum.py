# 1. Two Sum
#  ~15 minutes

from typing import List



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for  i in range(len(nums)):
            for j in range(len(nums)):
                
                if i == j:
                    continue


                if nums[i] + nums[j] == target:

                    return [i, j]


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9

    solution = Solution()
    solution.twoSum(
        nums, target
    )
        