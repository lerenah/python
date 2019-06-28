def pascals(n):
    output = [0, 1, 0]
    triangle = [output]
    i = 1
    while i in range(n):
        row = [0]
        for idx, el in enumerate(output):
            if idx + 1 in range(len(output)):
                row.append(el + output[idx + 1])
        row.append(0)
        triangle.append(row)
        output = row
        i += 1
    return triangle
