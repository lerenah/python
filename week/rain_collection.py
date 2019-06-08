def lesser_level(a, b):
    if a < b:
        return a
    elif b < a:
        return b
    else:
        return a


def second_highest(arr):
    maxed = arr[0]
    for el in arr:
        if el > maxed:
            maxed = el
    newArr = arr[:arr.index(maxed)]
    return maxed, newArr


def rain_collector(set_):
    highest = max(set_)
    valley = False
    contents = []
    water = 0
    counted = []
    for idx, num in enumerate(set_):
        i = idx + 1
        if i in range(len(set_)):
            if set_[i] < num:
                valley = True
                contents = []
                while valley and i in range(len(set_)):
                    if num == highest:
                        final, new_arr = second_highest(set_[set_.index(highest) + 1:])
                        for el in new_arr:
                            contents.append(el)
                        break
                    if set_[i] >= num:
                        final = set_[i]
                        counted.append(i)
                        break
                    contents.append(set_[i])
                    i += 1
            if valley and final != 0:
                levels = lesser_level(num, final)
                if len(counted) == 1:
                    for el in contents:
                        water += (levels - el)
                if idx == counted[0]:
                    for el in contents:
                        water += (levels - el)
                    valley = False
                    counted = []
                if set_.index(final) == (len(set_) - 1):
                    return water
                final = 0
    return water
