# https://leetcode.com/problems/length-of-last-word/
#  58. Length of Last Word
# Started at 15:05, finish at 15:10


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(list(filter(None, s.split(" ")))[-1])



if __name__ == "__main__":
    phrase  = " Hellor World "
    solution = Solution()
    print(solution.lengthOfLastWord(phrase))