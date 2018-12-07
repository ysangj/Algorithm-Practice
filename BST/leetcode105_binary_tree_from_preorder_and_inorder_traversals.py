# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def bt(pre, inor):
            if not pre:
                return
            
            mid = TreeNode(pre[0])
            
            #index of the head node in the inorder traversal array
            middex = inor.index(pre[0])
            
            #assign left of mid(head node) with only nodes on left side.
            #Note that nodes in left of middex in preorder array are all left-sided nodes.
            mid.left = bt(pre[1:middex + 1], inor[:middex])
            mid.right = bt(pre[middex + 1:], inor[middex + 1:])
            
            return mid
        return bt(preorder, inorder)