def dot_prod(matrix, vector):
    if not len(matrix[0]) == len(vector):
        return -1
    else:
        ans = []
        prod = []
        i = 0
        while i in range(len(matrix)):
            j = 0
            row = []
            while j in range(len(vector)):
                el = matrix[i][j] * vector[j]
                row.append(el)
                j += 1
            i += 1
            prod.append(row)

    for el in prod:
        ans.append(sum(el))


    return ans
