def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def reverse_words(message):
    if len(message) == 1:
        return message
    l = 0
    r = len(message) - 1
    words = message.count(' ')
    set_spaces = {}
    while l != r:
        swap(message, l, r)
        l += 1
        r -= 1
    curr = 0
    for i in range(len(message) + 1):
        if i == len(message) or message[i] == ' ':
            reverse(message, curr, i - 1)
            curr = i + 1
