def check_unival(root):
    if root.left_ptr is None and root.right_ptr is None:
        unival = True
        count = 1
    elif root.left_ptr and root.right_ptr is None:
        unival_left, count_left  = check_unival(root.left_ptr)
        if unival_left and root.val == root.left_ptr.val:
            unival = True
            count = count_left + 1
        else:
            unival = False
            count = count_left
    elif root.left_ptr is None and root.right_ptr:
        unival_right, count_right = check_unival(root.right_ptr)
        if unival_right and root.val == root.right_ptr.val:
            unival = True
            count = count_right + 1
        else:
            unival = False
            count = count_right
    else:
        unival_left, count_left  = check_unival(root.left_ptr)
        unival_right, count_right = check_unival(root.right_ptr)
        if (unival_left and unival_right) and (root.right_ptr.val == root.val and root.left_ptr.val == root.val):
            unival = True
            count = count_left + count_right + 1
        else:
            unival = False
            count = count_right + count_left

    return unival, count


def findSingleValueTrees(root):
    if not root:
        return 0
    _,res = check_unival(root)
    return res
