def sort_welsh(arr):
    idx = 0
    output = []
    for el in arr:
        if el[:2] in welsh_dict.keys():
            idx = welsh_dict[el[:2]]
        else:
            idx = welsh_dict[el[:1]]
        output.append((el, idx))
    output.sort(key=lambda x: x[1])
    return [x[0] for x in output]
