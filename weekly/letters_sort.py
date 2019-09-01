def letter_sort(string):
    # YOUR WORK HERE
    output = ''
    letters = [0] * 26
    num = 96
    counts = [0] * 26
    for i in range(len(letters)):
        letters[i] = num
        num += 1
    for j in range(len(string)):
        ord_string = ord(string[j])
        if counts[letters.index(ord_string)]:
            counts[letters.index(ord_string)] += 1
        else:
            counts[letters.index(ord_string)] = 1
    for i, el in enumerate(counts):
        for _ in range(el):
            output += chr(letters[i])
    return output
