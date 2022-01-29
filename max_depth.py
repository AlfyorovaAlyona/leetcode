from typing import List
from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        count_left = self.maxDepth(root.left)
        count_right = self.maxDepth(root.right)

        return count_right + 1 if count_right > count_left else count_left + 1


if __name__ == '__main__':
    sol = Solution()
