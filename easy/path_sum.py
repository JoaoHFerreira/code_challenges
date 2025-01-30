# https://leetcode.com/problems/path-sum/
# 112. Path Sum
from typing import Optional
from IPython import embed

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            if not root.left and not root.right:
                return root.val == targetSum
            
            total = 0
            last_val = 0
            is_left = True
            root.previous = None
            root.is_leaf = False
            root.is_root = True
            current_node = root
            while True:
                if current_node.left:
                    total += current_node.val

                    temp = current_node
                    current_node = current_node.left
                    current_node.is_root = False
                    current_node.previous = temp
                    continue

                if current_node.right:
                    total += current_node.val

                    temp = current_node
                    current_node = current_node.right
                    current_node.is_root = False
                    current_node.previous = temp
                    is_left = False
                    continue


                if current_node.left and current_node.right:
                    current_node.is_leaf = False
                else:
                    current_node.is_leaf = True


                total += current_node.val
                last_val = current_node.val


                if (
                    total == targetSum and
                    current_node.is_leaf and
                    not current_node.is_root
                    ):
                    return True
                
                total -= last_val
                current_node = current_node.previous

                if current_node:
                    total -= current_node.val
                    if is_left:
                        current_node.left = None
                        current_node.is_root = True
                    else:
                        current_node.right = None
                        current_node.is_root = True
                else:
                    return False
        return False
                





if __name__ == "__main__":
    test_cases = [
        {
            "target": 6,
            "root": TreeNode(
                val=1,
                right=TreeNode(
                    val=2,
                    right=TreeNode(
                        val=3,
                        right=TreeNode(
                            val=4,
                            right=TreeNode(
                                val=5,
                                left=None,
                                right=None,
                            ),
                            left=None,
                        ),
                    ),
                    left=None
                ),
                left=None
            )
        },
        {
            "target": 6,
            "root": TreeNode(
                val=1,
                left=TreeNode(
                    val=2,
                    left=TreeNode(
                        val=3,
                        left=TreeNode(
                            val=4,
                            left=TreeNode(
                                val=5,
                                left=None,
                                right=None,
                            ),
                            right=None,
                        ),
                    ),
                    right=None
                ),
                right=None
            )
        },
        {
            "target": 22,
            "root": TreeNode(
                val=5,
                left=TreeNode(
                    val=4,
                    left=TreeNode(
                        val=11,
                        left=TreeNode(
                            val=7,
                            left=None,
                            right=None
                        ), 
                        right=TreeNode(
                            val=2,
                            left=None,
                            right=None
                        )),
                    right=None
                ),
                right=TreeNode(
                    val=8,
                    left=TreeNode(
                        val=13,
                        left=None,
                        right=None
                    ),
                    right=TreeNode(
                        val=4,
                        left=None,
                        right=TreeNode(
                            val=1,
                            left=None, 
                            right=None
                        )
                    )
                )
            )
        },
        {
            "target": 1,
            "root": TreeNode(
                val=1,
                left=TreeNode(
                    val=2,
                    left=None,
                    right=None,
                ),
                right=None,
            )
        }
    ]

    solution = Solution()

    for test in test_cases:
        print(solution.hasPathSum(test.get("root"), test.get("target")))