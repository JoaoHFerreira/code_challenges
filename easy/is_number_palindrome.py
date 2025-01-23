# https://leetcode.com/problems/palindrome-number/
# 9. Palindrome Number
# Started at 10:20, paused at 10:41


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp = str(x)
        x_size = len(temp) -1

        palin_check = ""
        for i in range(x_size, -1, -1):
            palin_check += temp[i]
            
        palin_check = int(palin_check)

        return x == palin_check


if __name__ == "__main__":
    solution = Solution()
    solution.isPalindrome(121)