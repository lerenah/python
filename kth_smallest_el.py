def helper_func(tree, k, nodes):
    if tree is None:
        return
    if tree.left_ptr:
        helper_func(tree.left_ptr,k, nodes)
    nodes.append(tree.val)
    if tree.right_ptr:
        helper_func(tree.right_ptr, k, nodes)


def kth_smallest_element(root, k):
    nodes = []
    helper_func(root, k, nodes)
    return nodes[k]
