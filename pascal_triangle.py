# https://leetcode.com/problems/pascals-triangle/
# 118. Pascal's Triangle
# Started at 10:40, finish at  12:37

from typing import List
from IPython import embed



# 1. Coreners alwyas remain as one
# 2. Second layer increases 1 in each line
# 3. We just need to do halth of the process since is always a mirror
# 4. only the previous array to calculate, the rest can be stored in another array
# 5. Corner cases are, when 1 is [1]

# 1                                                        1
# 2                                                    1       1
# 3                                                1       2       1
# 4                                            1       3       3       1
# 5                                        1       4       6       4       1
# 6                                    1       5       10      10      5       1
# 7                                1       6       15      20      15      6       1
# 8                            1       7       21      35      35      21      7       1
# 9                        1       8       28      56      70      56      28       8     1
# 10                    1       9       36     84      126     126     84       36     9      1
                        
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        solution_array = []
        for i  in range(numRows):
            if i == 0:
                solution_array.append([1])

            else:
                reference_array = solution_array[-1]
                array_size = len(reference_array)

                temp_array = [1]
                mirrored_side_array = array_size // 2

                sum_pos_1, sum_pos_2 = 0, 1
                while mirrored_side_array:
                    if sum_pos_1 == mirrored_side_array:
                        break
                    temp_array.append(reference_array[sum_pos_1] +  reference_array[sum_pos_2])
                    sum_pos_1 += 1
                    sum_pos_2 += 1
                
                temp_array.extend(
                        sorted(temp_array, reverse=True)
                )

                if array_size % 2 == 0:   
                    del temp_array[len(temp_array) // 2]
            
                solution_array.append(temp_array)

        if numRows == 1:
            print(f"Passed with {numRows}")
            assert [[1]] == solution_array
   
        elif numRows == 2:
            print(f"Passed with {numRows}")
            assert [[1],[1,1]] == solution_array

        elif numRows == 3:
            print(f"Passed with {numRows}")
            assert [[1],[1,1],[1,2,1]] == solution_array

        elif numRows == 4:
            print(f"Passed with {numRows}")
            assert [[1],[1,1],[1,2,1],[1,3,3,1]] == solution_array
        
        elif numRows == 5:
            print(f"Passed with {numRows}")
            assert [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]] == solution_array


        


if __name__ == "__main__":
    solution = Solution()

    for i in range(1, 6):
        solution.generate(i)