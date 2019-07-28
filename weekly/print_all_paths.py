def printAllPaths(root, prefix=None):
    if root is None:
        return
    if prefix is None:
        prefix = []
    if root.left_ptr is None and root.right_ptr is None:
        print(' '.join(prefix + [str(root.val)]))
        return
    if root.left_ptr:
        printAllPaths(root.left_ptr, prefix + [str(root.val)])
    if root.right_ptr:
        printAllPaths(root.right_ptr, prefix + [str(root.val)])
