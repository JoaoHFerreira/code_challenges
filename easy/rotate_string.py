# https://leetcode.com/problems/rotate-string/  
# 796. Rotate String
from IPython import embed


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        Given an array of lettters, is the follow:
        1. If in last position move to zero
        2. If not, plus one the position
        3. The number of interactions with to find goal wil be always the (number of letters - 1), example:
           "abc" will have the follow rotations:
           3.1 "cab"
               -1 -> 0 
                0 -> 1, 
                1 -> 2
           3.2 "bca"
        """

        interactions = len(s)
        while interactions:
            embed()
            if s == goal:
                return True
            s = s[-1] + s[:-1]
            interactions -= 1

        return False



cccdd
dcccd
ddccc
cddcc
ccddc

if __name__ == "__main__":
    s, goal = "cccdd", "ccddc"

    solution = Solution()
    print(solution.rotateString(s, goal))