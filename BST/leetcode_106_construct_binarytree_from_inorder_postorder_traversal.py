# Construct Binary Tree from Inorder and Postorder Traversal

# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def totree(in_order, post_order):
            if not post_order:
                return
            
            root = TreeNode(post_order[-1])
            
            middex = in_order.index(post_order[-1])
            
            root.left = totree(in_order[:middex], post_order[:middex])
            root.right = totree(in_order[middex + 1:], post_order[middex : -1])

            return root
            
        return totree(inorder, postorder)