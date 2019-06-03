def getPermutations(array):
    if len(array) == 0:
        return []
    elif len(array) == 1:
        return array
    stopper = 1
    for i in range(stopper, len(array) + 1):
        stopper *= i

    else:
        output = []
        i = 0
        while len(output) != stopper:
            first = array[i]
            perm = [first]
            rest_of_array = list(filter(lambda x : x != first, array))
            j = 1
            while j <= len(rest_of_array):
              for el in rest_of_array:
                  perm.append(el)
              output.append(perm)
              perm = [first]
              rest_of_array.insert(0,rest_of_array.pop())
              j += 1
            i += 1

        return output
