class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # [A] searching tree by DFS
        def dfs(root: Optional[TreeNode], Sum: str) -> bool:

			# [A-1] if root is None -> no more searching
            if root == None:
                return 0

            Sum += str(root.val)
            left, right = root.left, root.right

            # [A-2] if root node, record Sum in result
            if left == None and right == None:
                result.append(int(Sum))
                return 0

			# [A-3] DFS searching both left and right side
            dfs(left, Sum)
            dfs(right, Sum)

		# [1] by DFS searching, we have Sums in result. And then, return sum of them.
        result = []
        dfs(root, '')
        return sum(result)