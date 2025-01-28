# https://leetcode.com/problems/roman-to-integer/
# 13. Roman to Integer


from IPython import embed
class Solution:
    N_MAP = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        letter_values = [self.N_MAP.get(value) for value in list(s)]
        list_size = len(s)

        total = 0
        check = None
        for i in range(list_size):

            if i == (list_size - 1) and check:
                break

            if i == (list_size - 1):
                total += letter_values[i]
                break

            if check:
                check = 0
                continue

            if letter_values[i+1] > letter_values[i]:
                total += (letter_values[i+1] - letter_values[i])
                check = 1

            else:
                total += letter_values[i]
                check = None
        
        return total

            



if __name__ == "__main__":
    # 1000 + 1000 - 100 + 100 - 10 + 10 - 1
    # M CM XC IX = 1999
    # roman_number = "M CM XC  IV"
    roman_number = "MCMXCIV"
    solution = Solution()
    print(solution.romanToInt(roman_number))
