# 88. Merge Sorted Array
# ~ 35 minutes

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        num2_inc = 0 
        for i in range(len(nums1)):

            if i >= m and n > 0:
                nums1[i] = nums2[num2_inc]
                num2_inc += 1
                n -= 1

        for i in range(len(nums1)):
            
            for j in range(len(nums1)):
                if i == j:
                    continue

                if nums1[i] < nums1[j]:
                    temp = nums1[j]
                    nums1[j] = nums1[i]
                    nums1[i] = temp


        assert nums1 == TARGET_VALUE, f"{nums1},\nexpected {TARGET_VALUE} instead)"


if __name__ == "__main__":
    TARGET_VALUE = [1,2,2,3,5,6]

    solution = Solution()
    solution.merge(
        nums1=[1,2,3,0,0,0],
        m=3,
        nums2=[2,5,6],
        n=3
    )
        