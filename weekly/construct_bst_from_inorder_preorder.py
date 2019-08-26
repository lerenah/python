def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        preorder_len = len(preorder)
        inorder_len = len(inorder)

        def helper(preStart, inStart, inEnd):
            if preStart > preorder_len - 1 or inStart > inEnd:
                return None
            root_val = preorder[preStart]
            root = TreeNode(root_val)
            print(root.val, ' is root')

            index = inorder.index(root.val)
            distance = (index - inStart) + 1

            root.left = helper(preStart + 1, inStart, index - 1 )
            root.right = helper(preStart + distance, index + 1, inEnd)
            return root

        return helper(0, 0, inorder_len - 1)
