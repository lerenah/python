def func(i, tree, s):
    if len(tree.children):
        while len(tree.children) != 0:
            if tree.left:
                tree = tree.children[s[i]]
                i += 1
            if tree.right:
                tree = tree.children[s[i]]
                i += 1
    return tree.data, i

def decode(s, tree):
    i = 0
    output_str = ''
    while i < len(s):
        char, i = func(i, tree, s)
        output_str += char

    return output_str
