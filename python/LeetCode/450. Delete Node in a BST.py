class Solution:

		# [A] key를 발견했을 때, 우측 자식 노드에서 가장 작은 값을 찾는 함수
    def findMinV(self, root: Optional[TreeNode]) -> int:
        minV = root.val
        while root.left:
            minV = root.left.val
            root = root.left
        return minV

		# [1] BST에서 key값을 갖는 노드를 삭제하는 함수
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
				# [2] key값인 노드를 찾았다면
        else:
		        # [3] 자식 노드가 한 쪽만 있을 때는 자식 노드를 그대로 땡겨온다.
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # [4] 자식 노드가 양쪽 존재할 때는 우측에서 가장 작은 자식 노드를 찾아 땡겨온다.
            else:
                root.val = self.findMinV(root.right)
                root.right = self.deleteNode(root.right, root.val)
                
        return root