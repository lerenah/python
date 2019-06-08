def has_valleys(arr):
    dips = False
    pending = False
    count_dips = 0
    if len(arr) < 1:
        return 0
    for idx, el in enumerate(arr):
        dips = False
        if idx in range(len(arr) - 1):
            if el > arr[idx + 1]:
                pending = True
            if pending:
                if el < arr[idx + 1]:
                    dips = True
                    pending = False
        if dips:
            count_dips += 1
    return count_dips


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
    if len(set_) == 0:
        return 0
    peak = False
    if set_.count(max(set_)) == 1:
        peak = True
        highest = max(set_)
    valley = False
    contents = []
    water = 0
    counted = []
    final = 0
    for idx, num in enumerate(set_):
        i = idx + 1
        if i in range(len(set_)):
            if set_[i] < num:
                valley = True
                contents = []
                while valley and i in range(len(set_)):
                    if peak:
                        if num == highest:
                            final, new_arr = second_highest(set_[set_.index(highest) + 1:])
                            for el in new_arr:
                                contents.append(el)
                            counted.append(set_.index(final))
                            break

                    if set_[i] >= num:
                        final = set_[i]
                        counted.append(i)
                        break
                    if i == (len(set_) - 1):
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
                if len(counted):
                    if idx == counted[0]:
                        for el in contents:
                            water += (levels - el)
                        valley = False
                        counted = list(filter(lambda x: x != idx, counted))
                if set_.index(final) == (len(set_) - 1):
                    return water
                final = 0
            elif i == (len(set_) - 1) and final == 0:
                if has_valleys(contents):
                    water += rain_collector(contents)
                    return water
                else:
                    return water
    return water
