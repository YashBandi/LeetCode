# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx={}
        for i,j in enumerate(preorder):
            idx[j]=i
        def helper(start,end,postorder):
        
            if end==start:
                return None
    
            if end-start==1:
                return TreeNode(postorder.pop())
    
        
            node=TreeNode(postorder.pop()) #3
            ind=idx[postorder[-1]] #4
        
            node.right=helper(ind,end,postorder) #1
            node.left=helper(start+1,ind,postorder) #2
            return node

        return helper(0,len(preorder),postorder)
        