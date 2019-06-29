# check scratch_1 file
def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)


def find_first(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return None
    if source[index - 1] == target:
        while source[index] == target:
            index -= 1
        return index + 1
    return index
