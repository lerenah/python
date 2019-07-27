def get_left(tree):
    while tree.left_ptr is not None:
        tree = tree.left_ptr
    return tree


def get_right(tree):
    while tree.right_ptr is not None:
        tree = tree.right_ptr
    return tree


def get_successor(tree):
    if tree is None:
        return None
    if tree.right_ptr is not None:
        return get_left(tree.right_ptr)
    parent = tree.parent
    while parent.left_ptr != tree:
        tree = parent
        parent = tree.parent
        if parent is None:
            return None
    return parent


def helper(tree, parent=None):
    if tree is None:
        return None
    tree.parent = parent
    helper(tree.left_ptr, tree)
    helper(tree.right_ptr, tree)


def copy(node):
    return TreeNode(val=node.val)


def BTtoLL(root):
    # store parent pointers
    if root is None:
        return
    helper(root)
    start = get_left(root)
    end = get_right(root)
    LLstart = copy(start)
    LLcurrent = LLstart
    current = start
    while current != end:
        _next = get_successor(current)
        LLnext = copy(_next)
        LLcurrent.right_ptr = LLnext
        LLnext.left_ptr = LLcurrent
        LLcurrent = LLnext
        current = _next

    LLcurrent.right_ptr = LLstart
    LLstart.left_ptr = LLcurrent
    return LLstart
