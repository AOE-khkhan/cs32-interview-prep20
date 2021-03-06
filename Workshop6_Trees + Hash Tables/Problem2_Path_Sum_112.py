"""
    UCLA ACM ICPC: Interview Track Leetcode Problem Solutions

    Disclaimer: This is not the only valid solution and we do not claim our solutions
    to be optimal in terms of runtime or memory usage, we are merely giving example
    solutions to questions for learning purposes only

    Path Sum
    Leetcode Problem 112
    https://leetcode.com/problems/path-sum/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.
"""

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        Base case: If the root is NULL, then
        there are no nodes that can add up to
        the given sum, so we return false.
        """

        if root == None:
            return False

        left = root.left
        right = root.right
        val = root.val

        """
        The root is a leaf if its left and right
        subtree are both NULL. We can then check if
        the leaf value equals the given sum. If this
        passes, we can return true, because the root
        to leaf path (which is just the root itself)
        equals the sum.
        """
        if left == None and right == None and val == sum:
            return True
        """
        Recursive case: All possible root to leaf paths must go through
        the root, so to check if a root to leaf path exists that adds
        up to the given sum, it suffices to check if there is a left
        or right subroot to leaf path that adds up to sum minus the value
        of the root node.
        """
        return self.hasPathSum(left, sum - val) or self.hasPathSum(right, sum - val)

"""
Time Complexity Analysis:
We examine each node at most twice: once if is ever the root of an examined
subtree, and once if it is ever the child of the a subtree's root. If there are
n nodes, then we do at most 2n examinations, meaning our runtime is O(n).
"""