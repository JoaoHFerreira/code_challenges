# https://leetcode.com/problems/valid-palindrome/
# 125. Valid Palindrome



class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_list = """ .,:@}{][#_-'\/" ?!;()`´"""

        reduced_list = list(filter(lambda x:  x not in char_list, list(s.lower())))

        cleaned_version = "".join(reduced_list)
        palindrome_version = "".join(reversed(reduced_list))
        

        return palindrome_version ==  cleaned_version


if __name__ == "__main__":
    phrase = "A man, a plan, a canal: Panama"
    solution = Solution()
    print(solution.isPalindrome(phrase))