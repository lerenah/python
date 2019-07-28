def diameterOfBinaryTree(root):
    num = 0

    def helper_function(root):
        if root is None:
            return 0
        left = helper_function(root.left)
        right = helper_function(root.right)
        num = max(num, left + right)
        return max(left, right) + 1

    helper_function(root)
    return num
