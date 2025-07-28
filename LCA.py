class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
            return root
        if p.val == root.val or q.val == root.val:
            return root
        if p.val < root.val and q.val < root.val: #both are smaller than root, so search left
            return self.lowestCommonAncestor(root.left, p, q)
        else: #both values are bigger than root
            return self.lowestCommonAncestor(root.right, p, q)


sol = Solution()        
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
p = root.right   # Node with value 3
q = root.left    # Node with value 1

print(sol.lowestCommonAncestor(root, p, q).val)
