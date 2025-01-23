# https://leetcode.com/problems/plus-one/
# 66. Plus One
# Started at 11:48, finish at  11:55
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus_one_list = list(map(int, list(str(int("".join(list(map(str, digits)))) + 1))))        

        assert [4, 3, 2, 2] == plus_one_list



if __name__ == "__main__":
    phrase  = [4, 3, 2, 1]
    solution = Solution()
    solution.plusOne(phrase)

