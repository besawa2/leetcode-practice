# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# declare n to tell us how many elements we've visited. n==k means we are on the kth value
# stack = [], and a pointer curr
# while current is not null, and the stack is nonempty, traverse
# to traverse: while current is not null or the stack is not empty, add current to stack, and set current to left 
# when the 2nd while loop exits, that means cur is null, so we pop last element from stack (most recently added)
# we set that popped element to cur to "process" it, so we increment n and do our check with k to see if we need to return cur.val
# if not the case, we should visit the right subtree and set cur to right
# dont need a return outside of the 1st while, as there will always be at least k elements
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            n += 1

            if n == k:
                return curr.val
            
            curr = curr.right