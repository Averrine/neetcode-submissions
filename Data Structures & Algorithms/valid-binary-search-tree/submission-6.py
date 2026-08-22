# Definition for a binary tree node.
# class Node:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[Node]) -> bool:
        def Valid(Node, low, high):
            if Node is None:
                return True
            if Node.val <= low or Node.val >= high:
                return False
            return Valid(Node.left, low, Node.val) and Valid(Node.right, Node.val, high)

        return Valid(root, float('-inf'), float('inf'))
            
