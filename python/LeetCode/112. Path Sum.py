class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # [A] searching tree by DFS
        def dfs(root: Optional[TreeNode], Sum: int) -> bool:

						# [A-1] if root is None -> no more searching
            if root == None:
                return 0

            Sum += root.val
            left, right = root.left, root.right

            # [A-2] if root node, record Sum in result
            if left == None and right == None:
                result.append(Sum)
                return 0

			# [A-3] DFS searching both left and right side
            dfs(left, Sum)
            dfs(right, Sum)

		# [1] by DFS searching, we have Sums in result. And then, if we have targetSum in result, return True
        result = []
        dfs(root, 0)
        if targetSum in result:
            return True
        return False