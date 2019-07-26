def helper_func(a, start, end):
    if start > end:
        return None
    mid = start + (end - start) // 2
    root = TreeNode(a[mid])
    root.left_ptr = helper_func(a, start, mid - 1)
    root.right_ptr = helper_func(a, mid + 1, end)
    return root

def build_balanced_bst(a):
    return helper_func(a, 0, len(a) - 1)
