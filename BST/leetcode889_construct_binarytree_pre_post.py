# 889. Construct Binary Tree from Preorder and Postorder Traversal

# Return any binary tree that matches the given preorder and postorder traversals.

# Values in the traversals pre and post are distinct positive integers.

 

# Example 1:

# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
 

# Note:

# 1 <= pre.length == post.length <= 30
# pre[] and post[] are both permutations of 1, 2, ..., pre.length.
# It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        def build(preorder, postorder):
            if not preorder:
                return None
            if not postorder:
                return None
            if len(preorder) == 1:
                return TreeNode(preorder[0])
            if len(postorder) == 1:
                return TreeNode(postorder[-1])
            
            root = TreeNode(preorder[0])
            
            post_last = postorder[-2]
            
            dex = preorder.index(post_last) - 1

            root.left = build(preorder[1:dex + 1], postorder[:dex])
            root.right = build(preorder[dex + 1:], postorder[dex:-1])
            return root
        return build(pre, post)            