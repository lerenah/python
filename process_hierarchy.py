def process_root(arr):
    _arr = list(filter(lambda x: len(x[0]['children']), arr))
    for el in _arr:
        root = el[0][id]
        i = 1
        while i < len(_arr):
            if root in _arr[i][0]['children']:
                root = _arr[i][0][id]
            i += 1

    return root




